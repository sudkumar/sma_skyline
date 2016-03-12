# Stable Marriage Algorithm (SMA) using Skylines

#### Clone the project using recursive option
  
	git clone --recursive https://github.com/sudkumar/sma_skyline

#### Generate sample data files

> python data.py num\_of\_rows quality\_dims require\_dims

	python data.py 500 4 6

This will create two files aData.txt and bData.txt for both sets. And this will also create the query file. Now run

	python run.py

This will put matching ids into skyline.txt like this:

	ai.id bj.id
	ak.id bl.id

here a(x).id matched with b(y).id  

### Create the preference table

> Prints the rank list of all women for a man and of all men for a women in list format. Make sure the data files are been create before running this

    python pref_table.py



### Compute Score for both the algorith

> Computes the score of both the algorithm and prints in a list format. Lower the score, better is the matching. Make sure both the algorithm's output files are genereated

    python computeScore.py