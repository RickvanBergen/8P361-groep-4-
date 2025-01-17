import os
from keras.models import model_from_json
from keras.callbacks import ModelCheckpoint, TensorBoard


def load_pr_model(name):
    path = os.path.join('models','Prediction_mod',name)
    with open(path + '.json', 'r') as f:
        model = model_from_json(f.read())
    model.load_weights(path + '_weights.hdf5')
    return model

def load_com_model(name):
    path = os.path.join('models','Combination_mod',name)
    with open(path + '.json', 'r') as f:
        model = model_from_json(f.read())
    model.load_weights(path + '_weights.hdf5')
    return model

def save_com_model(name,model):
    model_name = os.path.join('models\Combination_mod',name)
    model_filepath = model_name + '.json'
    weights_filepath = model_name + '_weights.hdf5'

    model_json = model.to_json()
    with open(model_filepath, 'w') as json_file:
        json_file.write(model_json)
        model.save_weights(weights_filepath)
    checkpoint = ModelCheckpoint(weights_filepath, monitor='val_loss', verbose=1, save_best_only=True, mode='min')
    tensorboard = TensorBoard(os.path.join('logs', model_name))
    callbacks_list = [checkpoint, tensorboard]
    return callbacks_list