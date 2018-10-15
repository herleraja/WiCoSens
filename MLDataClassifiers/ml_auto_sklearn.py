import autosklearn.classification
import ml_utils
from sklearn.metrics import accuracy_score

(train_container_data, train_container_labels, train_container_labels_raw), (
    train_rack_data, train_rack_labels, train_rack_labels_raw) = ml_utils.get_trainig_data()
(test_rack_data, test_rack_labels, test_rack_labels_raw), (
    test_container_data, test_container_labels, test_container_labels_raw) = ml_utils.get_testing_data()

automl = autosklearn.classification.AutoSklearnClassifier(
    #time_left_for_this_task=120, per_run_time_limit=30,
    tmp_folder='/home/herle/WiCoSens/MLDataClassifiers/autoslearn_sequential_example_tmp',
    output_folder='/home/herle/WiCoSens/MLDataClassifiers/autosklearn_sequential_example_out',
    # Do not construct ensembles in parallel to avoid using more than one
    # core at a time. The ensemble will be constructed after auto-sklearn
    # finished fitting all machine learning models.
    ensemble_size=0, delete_tmp_folder_after_terminate=False)
automl.fit(train_container_data, train_container_labels_raw)

# This call to fit_ensemble uses all models trained in the previous call
# to fit to build an ensemble which can be used with automl.predict()
automl.fit_ensemble(train_container_labels_raw, ensemble_size=50)

print(automl.show_models())
test_predicted_container_res = automl.predict(test_container_data)
print(automl.sprint_statistics())
print("Accuracy score", accuracy_score(test_container_labels_raw, test_predicted_container_res))
