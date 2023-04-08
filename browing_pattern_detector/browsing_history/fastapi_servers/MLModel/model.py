import pickle
filename = 'svm_stem(3,3).sav'


def prediction(URL):
    model = pickle.load(open('svm_stem(3,3).sav', 'rb'))
    result = model.predict([URL])[0]
    return result