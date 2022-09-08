package hex.pipeline;

import hex.Model;
import hex.ModelBuilder;
import hex.ModelCategory;
import hex.pipeline.DataTransformer.FrameType;
import hex.pipeline.PipelineContext.CompositeFrameTracker;
import hex.pipeline.PipelineContext.ConsistentKeyTracker;
import hex.pipeline.PipelineModel.PipelineOutput;
import hex.pipeline.PipelineModel.PipelineParameters;
import water.Key;
import water.Keyed;
import water.fvec.Frame;


public class Pipeline extends ModelBuilder<PipelineModel, PipelineParameters, PipelineOutput> {
  
  public Pipeline(PipelineParameters parms) {
    super(parms);
    init(false);
  }

  public Pipeline(PipelineParameters parms, Key<PipelineModel> key) {
    super(parms, key);
  }

  public Pipeline(boolean startup_once) {
    super(new PipelineParameters(), startup_once, null);  // no schema directory to completely disable schema lookup for now.
  }

  @Override
  public void init(boolean expensive) {
    if (expensive) {
      earlyValidateParams();
    }
    super.init(expensive);
  }
  
  protected void earlyValidateParams() {
    if (_parms._categorical_encoding != Model.Parameters.CategoricalEncodingScheme.AUTO) {
      // we need to ensure that no transformation occurs before the transformers in the pipeline
      hide("_categorical_encoding",
           "Pipeline supports only AUTO categorical encoding: custom categorical encoding should be applied either as a transformer or directly to the final estimator of the pipeline.");
      _parms._categorical_encoding = Model.Parameters.CategoricalEncodingScheme.AUTO;
    }
    if (_parms._transformers == null) _parms._transformers = new DataTransformer[0];
  }

  @Override
  protected PipelineDriver trainModelImpl() {
    return new PipelineDriver();
  }

  @Override
  public ModelCategory[] can_build() {
    ModelBuilder finalBuilder = getFinalBuilder();
    return finalBuilder == null ? new ModelCategory[] {ModelCategory.Unknown} : finalBuilder.can_build();
//    return finalBuilder == null ? ModelCategory.values() : finalBuilder.can_build();
  }

  @Override
  public boolean isSupervised() {
    ModelBuilder finalBuilder = getFinalBuilder();
    return finalBuilder != null && finalBuilder.isSupervised();
  }
  
  private ModelBuilder getFinalBuilder() {
    return _parms._estimator == null ? null : ModelBuilder.make(_parms._estimator.algoName(), null, null);
  }
  
  //TODO: probably disable parallelization for CV
  
  public class PipelineDriver extends Driver {
    @Override
    public void computeImpl() {
      init(true);
      PipelineOutput output = new PipelineOutput(Pipeline.this);
      PipelineModel model = new PipelineModel(dest(), _parms, output);
      output._transformers = _parms._transformers.clone();
      model.delete_and_lock(_job);
      try {
//        DataTransformer lastTransformer = _parms._transformers[_parms._transformers.length - 1];
        PipelineContext context = new PipelineContext(_parms, new CompositeFrameTracker(
                new ConsistentKeyTracker(),
                new PipelineContext.FrameTracker() {
                  @Override
                  public void apply(Frame transformed, Frame frame, FrameType type, PipelineContext context, DataTransformer transformer) {
                    boolean useScope = !_parms._is_cv_model;
                    trackFrame(transformed, useScope);
                  }
                }
        ));
        TransformerChain chain = new TransformerChain(_parms._transformers);
        chain.prepare(context);
        setTrain(context.getTrain());
        setValid(context.getValid());
        if (_parms._estimator == null) return;
        output._estimator = chain.transform(
                new Frame[]{train(), valid()},
                new FrameType[]{FrameType.Training, FrameType.Validation},
                context,
                (frames, ctxt) -> {
                  // propagate data params only
                  _parms._estimator._train = frames[0] == null ? null : frames[0].getKey();
                  _parms._estimator._valid = frames[1] == null ? null : frames[1].getKey();
                  _parms._estimator._response_column = _parms._response_column;
                  _parms._estimator._fold_column = _parms._fold_column;
                  _parms._estimator._weights_column = _parms._weights_column;
                  _parms._estimator._offset_column = _parms._offset_column;
                  Keyed res = ModelBuilder.make(_parms._estimator).trainModel().get();
                  return res == null ? null : res.getKey();
                }
        );
      } finally {
        model.update(_job);
        model.unlock(_job);
      }
    }
    
  }

  @Override
  public void computeCrossValidation() {
    new TransformerChain(_parms._transformers).prepare(new PipelineContext(_parms));
    super.computeCrossValidation();
  }

}
