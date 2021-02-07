import pandas as pd
import matplotlib.pyplot as plt


def main():
	data = pd.read_csv('titanic_data/train.csv')
	print(data.head())
	print(data.count())

	# plot the figure
	plt.figure(figsize=(18,7))

	plt.subplot2grid((3, 4), (0, 0))
	data.Survived.value_counts(normalize=True).sort_index().plot(kind='bar')
	plt.title('Survived')

	plt.subplot2grid((3, 4), (0, 1))
	data.Pclass.value_counts(normalize=True).plot(kind='pie')

	plt.subplot2grid((3, 4), (0, 2))
	data.Pclass[data.Survived == 1].value_counts(normalize=True).sort_index().plot(kind='bar', color='green')
	plt.title('Pclass Survived')

	plt.subplot2grid((3, 4), (0, 3))
	data.Pclass[data.Survived == 0].value_counts(normalize=True).sort_index().plot(kind='bar', color='gray')
	plt.title('Pclass NonSurvived')

	plt.subplot2grid((3, 4), (1, 0))
	data.Survived[data.Sex == 'male'].value_counts(normalize=True).sort_index().plot(kind='bar', color='tab:blue')
	plt.title('Men Survived')

	plt.subplot2grid((3, 4), (1, 1))
	data.Survived[data.Sex == 'female'].value_counts(normalize=True).sort_index().plot(kind='bar', color='m')
	plt.title('Women Survived')

	plt.subplot2grid((3, 4), (1, 2))
	data.Sex.value_counts(normalize=True).sort_index().plot(kind='bar')
	plt.title('Sex')

	plt.subplot2grid((3, 4), (1, 3))
	data.Age[data.Survived == 1].plot(kind='hist')
	plt.title('Survived Age')

	plt.subplot2grid((3, 4), (2, 0))
	data.Survived[(data.Sex == 'male') & (data.Pclass == 1)].value_counts(normalize=True).sort_index().plot(kind='bar', color='dodgerblue')
	plt.title('Rich Men Survived')

	plt.subplot2grid((3, 4), (2, 1))
	data.Survived[(data.Sex == 'male') & (data.Pclass == 3)].value_counts(normalize=True).sort_index().plot(kind='bar', color='navy')
	plt.title('Poor Men Survived')

	plt.subplot2grid((3, 4), (2, 2))
	data.Survived[(data.Sex == 'female') & (data.Pclass == 1)].value_counts(normalize=True).sort_index().plot(kind='bar', color='violet')
	plt.title('Rich Women Survived')

	plt.subplot2grid((3, 4), (2, 3))
	data.Survived[(data.Sex == 'female') & (data.Pclass == 3)].value_counts(normalize=True).sort_index().plot(kind='bar', color='darkred')
	plt.title('Poor Women Survived')

	# plt.subplot2grid((3, 4), (2, 1))
	# plt.plot(kind='scatter', x=data.Pclass, y=data.Survived)

	# plt.subplot2grid((3, 4), (2, 2))
	# data.Fare.plot(kind='kde')






	plt.show()


if __name__ == '__main__':
	main()