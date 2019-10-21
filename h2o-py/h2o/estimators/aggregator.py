#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# This file is auto-generated by h2o-3/h2o-bindings/bin/gen_python.py
# Copyright 2016 H2O.ai;  Apache License Version 2.0 (see LICENSE for details)
#
from __future__ import absolute_import, division, print_function, unicode_literals

from h2o.estimators.estimator_base import H2OEstimator
from h2o.exceptions import H2OValueError
from h2o.frame import H2OFrame
from h2o.utils.typechecks import assert_is_type, Enum, numeric


class H2OAggregatorEstimator(H2OEstimator):
    """
    Aggregator

    """

    algo = "aggregator"
    param_names = {"model_id", "training_frame", "response_column", "ignored_columns", "ignore_const_cols",
                   "target_num_exemplars", "rel_tol_num_exemplars", "transform", "categorical_encoding",
                   "save_mapping_frame", "num_iteration_without_new_exemplar", "export_checkpoints_dir"}

    def __init__(self, **kwargs):
        super(H2OAggregatorEstimator, self).__init__()
        self._parms = {}
        for pname, pvalue in kwargs.items():
            if pname == 'model_id':
                self._id = pvalue
                self._parms["model_id"] = pvalue
            elif pname in self.param_names:
                # Using setattr(...) will invoke type-checking of the arguments
                setattr(self, pname, pvalue)
            else:
                raise H2OValueError("Unknown parameter %s = %r" % (pname, pvalue))
        self._parms["_rest_version"] = 99

    @property
    def training_frame(self):
        """
        Id of the training data frame.

        Type: ``H2OFrame``.

        :examples:

        >>> cars = h2o.import_file("https://s3.amazonaws.com/h2o-public-test-data/smalldata/junit/cars_20mpg.csv")
        >>> cars["economy_20mpg"] = cars["economy_20mpg"].asfactor()
        >>> predictors = ["displacement","power","weight","acceleration","year"]
        >>> response_column = "economy_20mpg"
        >>> train, valid = cars.split_frame(ratios = [.8], seed = 1234)
        >>> cars_ag = H2OAggregatorEstimator()
        >>> cars_ag.train(x = predictors,
        ...               y = response_column,
        ...               training_frame = train,
        ...               validation_frame = valid)
        >>> cars_ag.aggregated_frame
        """
        return self._parms.get("training_frame")

    @training_frame.setter
    def training_frame(self, training_frame):
        self._parms["training_frame"] = H2OFrame._validate(training_frame, 'training_frame')


    @property
    def response_column(self):
        """
        Response variable column.

        Type: ``str``.
        """
        return self._parms.get("response_column")

    @response_column.setter
    def response_column(self, response_column):
        assert_is_type(response_column, None, str)
        self._parms["response_column"] = response_column


    @property
    def ignored_columns(self):
        """
        Names of columns to ignore for training.

        Type: ``List[str]``.
        """
        return self._parms.get("ignored_columns")

    @ignored_columns.setter
    def ignored_columns(self, ignored_columns):
        assert_is_type(ignored_columns, None, [str])
        self._parms["ignored_columns"] = ignored_columns


    @property
    def ignore_const_cols(self):
        """
        Ignore constant columns.

        Type: ``bool``  (default: ``True``).

        :examples:

        >>> cars = h2o.import_file("https://s3.amazonaws.com/h2o-public-test-data/smalldata/junit/cars_20mpg.csv")
        >>> cars["economy_20mpg"] = cars["economy_20mpg"].asfactor()
        >>> predictors = ["displacement","power","weight","acceleration","year"]
        >>> response = "economy_20mpg"
        >>> cars["const_1"] = 6
        >>> cars["const_2"] = 7
        >>> train, valid = cars.split_frame(ratios = [.8], seed = 1234)
        >>> cars_ag = H2OAggregatorEstimator(ignore_const_cols = True)
        >>> cars_ag.train(x = predictors,
        ...               y = response,
        ...               training_frame = train,
        ...               validation_frame = valid)
        >>> cars_ag.aggregated_frame
        """
        return self._parms.get("ignore_const_cols")

    @ignore_const_cols.setter
    def ignore_const_cols(self, ignore_const_cols):
        assert_is_type(ignore_const_cols, None, bool)
        self._parms["ignore_const_cols"] = ignore_const_cols


    @property
    def target_num_exemplars(self):
        """
        Targeted number of exemplars

        Type: ``int``  (default: ``5000``).

        :examples:

        >>> cars = h2o.import_file("https://s3.amazonaws.com/h2o-public-test-data/smalldata/junit/cars_20mpg.csv")
        >>> cars["economy_20mpg"] = cars["economy_20mpg"].asfactor()
        >>> predictors = ["displacement","power","weight","acceleration","year"]
        >>> response_column = "economy_20mpg"
        >>> train, valid = cars.split_frame(ratios = [.8], seed = 1234)
        >>> cars_ag = H2OAggregatorEstimator(target_num_exemplars = 5000)
        >>> cars_ag.train(x = predictors,
        ...               y = response_column,
        ...               training_frame = train,
        ...               validation_frame = valid)
        >>> cars_ag.aggregated_frame
        """
        return self._parms.get("target_num_exemplars")

    @target_num_exemplars.setter
    def target_num_exemplars(self, target_num_exemplars):
        assert_is_type(target_num_exemplars, None, int)
        self._parms["target_num_exemplars"] = target_num_exemplars


    @property
    def rel_tol_num_exemplars(self):
        """
        Relative tolerance for number of exemplars (e.g, 0.5 is +/- 50 percents)

        Type: ``float``  (default: ``0.5``).

        :examples:

        >>> cars = h2o.import_file("https://s3.amazonaws.com/h2o-public-test-data/smalldata/junit/cars_20mpg.csv")
        >>> cars["economy_20mpg"] = cars["economy_20mpg"].asfactor()
        >>> predictors = ["displacement","power","weight","acceleration","year"]
        >>> response = "economy_20mpg"
        >>> train, valid = cars.split_frame(ratios = [.8], seed = 1234)
        >>> cars_ag = H2OAggregatorEstimator(rel_tol_num_exemplars = .7)
        >>> cars_ag.train(x = predictors,
        ...               y = response,
        ...               training_frame = train,
        ...               validation_frame = valid)
        >>> cars_ag.aggregated_frame
        """
        return self._parms.get("rel_tol_num_exemplars")

    @rel_tol_num_exemplars.setter
    def rel_tol_num_exemplars(self, rel_tol_num_exemplars):
        assert_is_type(rel_tol_num_exemplars, None, numeric)
        self._parms["rel_tol_num_exemplars"] = rel_tol_num_exemplars


    @property
    def transform(self):
        """
        Transformation of training data

        One of: ``"none"``, ``"standardize"``, ``"normalize"``, ``"demean"``, ``"descale"``  (default: ``"normalize"``).

        :examples:

        >>> cars = h2o.import_file("https://s3.amazonaws.com/h2o-public-test-data/smalldata/junit/cars_20mpg.csv")
        >>> cars["economy_20mpg"] = cars["economy_20mpg"].asfactor()
        >>> predictors = ["displacement","power","weight","acceleration","year"]
        >>> response_column = "economy_20mpg"
        >>> train, valid = cars.split_frame(ratios = [.8], seed = 1234)
        >>> cars_ag = H2OAggregatorEstimator(transform = "demean")
        >>> cars_ag.train(x = predictors,
        ...               y = response_column,
        ...               training_frame = train,
        ...               validation_frame = valid)
        >>> cars_ag.aggregated_frame
        """
        return self._parms.get("transform")

    @transform.setter
    def transform(self, transform):
        assert_is_type(transform, None, Enum("none", "standardize", "normalize", "demean", "descale"))
        self._parms["transform"] = transform


    @property
    def categorical_encoding(self):
        """
        Encoding scheme for categorical features

        One of: ``"auto"``, ``"enum"``, ``"one_hot_internal"``, ``"one_hot_explicit"``, ``"binary"``, ``"eigen"``,
        ``"label_encoder"``, ``"sort_by_response"``, ``"enum_limited"``  (default: ``"auto"``).

        :examples:

        >>> airlines= h2o.import_file("https://s3.amazonaws.com/h2o-public-test-data/smalldata/airlines/allyears2k_headers.zip")
        >>> airlines["Year"]= airlines["Year"].asfactor()
        >>> airlines["Month"]= airlines["Month"].asfactor()
        >>> airlines["DayOfWeek"] = airlines["DayOfWeek"].asfactor()
        >>> airlines["Cancelled"] = airlines["Cancelled"].asfactor()
        >>> airlines['FlightNum'] = airlines['FlightNum'].asfactor()
        >>> predictors = ["Origin", "Dest", "Year", "UniqueCarrier",
        ...               "DayOfWeek", "Month", "Distance", "FlightNum"]
        >>> response = "IsDepDelayed"
        >>> train, valid= airlines.split_frame(ratios = [.8], seed = 1234)
        >>> encoding = "one_hot_explicit"
        >>> airlines_ag = H2OAggregatorEstimator(categorical_encoding = encoding)
        >>> airlines_ag.train(x = predictors,
        ...                   y = response,
        ...                   training_frame = train,
        ...                   validation_frame = valid)
        >>> airlines_ag.aggregated_frame
        """
        return self._parms.get("categorical_encoding")

    @categorical_encoding.setter
    def categorical_encoding(self, categorical_encoding):
        assert_is_type(categorical_encoding, None, Enum("auto", "enum", "one_hot_internal", "one_hot_explicit", "binary", "eigen", "label_encoder", "sort_by_response", "enum_limited"))
        self._parms["categorical_encoding"] = categorical_encoding


    @property
    def save_mapping_frame(self):
        """
        Whether to export the mapping of the aggregated frame

        Type: ``bool``  (default: ``False``).

        :examples:

        >>> cars = h2o.import_file("https://s3.amazonaws.com/h2o-public-test-data/smalldata/junit/cars_20mpg.csv")
        >>> cars["economy_20mpg"] = cars["economy_20mpg"].asfactor()
        >>> predictors = ["displacement","power","weight","acceleration","year"]
        >>> response_column = "economy_20mpg"
        >>> train, valid = cars.split_frame(ratios = [.8], seed = 1234)
        >>> cars_ag = H2OAggregatorEstimator(save_mapping_frame = True)
        >>> cars_ag.train(x = predictors,
        ...               y = response_column,
        ...               training_frame = train,
        ...               validation_frame = valid)
        >>> cars_ag.aggregated_frame
        >>> cars_ag.save_mapping_frame
        """
        return self._parms.get("save_mapping_frame")

    @save_mapping_frame.setter
    def save_mapping_frame(self, save_mapping_frame):
        assert_is_type(save_mapping_frame, None, bool)
        self._parms["save_mapping_frame"] = save_mapping_frame


    @property
    def num_iteration_without_new_exemplar(self):
        """
        The number of iterations to run before aggregator exits if the number of exemplars collected didn't change

        Type: ``int``  (default: ``500``).

        :examples:

        >>> airlines= h2o.import_file("https://s3.amazonaws.com/h2o-public-test-data/smalldata/airlines/allyears2k_headers.zip")
        >>> airlines["Year"]= airlines["Year"].asfactor()
        >>> airlines["Month"]= airlines["Month"].asfactor()
        >>> airlines["DayOfWeek"] = airlines["DayOfWeek"].asfactor()
        >>> airlines["Cancelled"] = airlines["Cancelled"].asfactor()
        >>> airlines['FlightNum'] = airlines['FlightNum'].asfactor()
        >>> predictors = airlines.columns[:9]
        >>> response = "IsDepDelayed"
        >>> train, valid= airlines.split_frame(ratios = [.8], seed = 1234)
        >>> col_list = ['DepTime','CRSDepTime','ArrTime','CRSArrTime']
        >>> airlines_ag = H2OAggregatorEstimator(num_iteration_without_new_exemplar = 500)
        >>> airlines_ag.train(y = response,
        ...                   training_frame = train,
        ...                   validation_frame = valid)
        >>> airlines_ag.aggregated_frame
        """
        return self._parms.get("num_iteration_without_new_exemplar")

    @num_iteration_without_new_exemplar.setter
    def num_iteration_without_new_exemplar(self, num_iteration_without_new_exemplar):
        assert_is_type(num_iteration_without_new_exemplar, None, int)
        self._parms["num_iteration_without_new_exemplar"] = num_iteration_without_new_exemplar


    @property
    def export_checkpoints_dir(self):
        """
        Automatically export generated models to this directory.

        Type: ``str``.

        :examples:

        >>> import tempfile
        >>> from os import listdir
        >>> airlines = h2o.import_file("http://s3.amazonaws.com/h2o-public-test-data/smalldata/airlines/allyears2k_headers.zip", destination_frame="air.hex")
        >>> predictors = ["DayofMonth", "DayOfWeek"]
        >>> response = "IsDepDelayed"
        >>> checkpoints_dir = tempfile.mkdtemp()
        >>> airlines_ag = H2OAggregatorEstimator()
        >>> airlines_ag.train(x = predictors,
        ...                   y = response,
        ...                   training_frame = airlines)
        >>> len(listdir(checkpoints_dir))
        """
        return self._parms.get("export_checkpoints_dir")

    @export_checkpoints_dir.setter
    def export_checkpoints_dir(self, export_checkpoints_dir):
        assert_is_type(export_checkpoints_dir, None, str)
        self._parms["export_checkpoints_dir"] = export_checkpoints_dir


    @property
    def aggregated_frame(self):
        if (self._model_json is not None
                and self._model_json.get("output", {}).get("output_frame", {}).get("name") is not None):
            out_frame_name = self._model_json["output"]["output_frame"]["name"]
            return H2OFrame.get_frame(out_frame_name)
