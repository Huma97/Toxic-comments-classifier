from utils import *
import pickle
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('comment', type=str, help='write your comment')
args = parser.parse_args()

def main():

  comment = args.comment

  comment = comment.lower()
  comment = cleanPunc(comment)
  comment = keepAlpha(comment)
  comment = removeStopWords(comment)
  comment = stem(comment)

  vectorizer = pickle.load(open("vectorizer.pk", "rb" ) )

  comment = vectorizer.transform([comment])

  model = pickle.load(open('final_classifier.sav', 'rb'))

  predictions = model.predict(comment)[0]

  targets = ['toxic', 'severe toxic', 'obscene', 'threat', 'insult', 'identity_hate']

  for i, prediction in enumerate(predictions):
    if prediction == 1:
      print('This comment is {} \n'.format(targets[i]))
    else:
      print('This comment is not {} \n'.format(targets[i]))

if __name__ == '__main__':
  main()

