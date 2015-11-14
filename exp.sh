#!/bin/ bash

ROWS=(
	1500 2000 2500 3000 3500 4000 4500 5000
	)

qDIMS=(2 3 4 5)
rDIMS=(2 3 4 5)


rows=1000

echo Q$'\t'R$'\t'T > dims1.txt
echo Q$'\t'R$'\t'T > dims2.txt
# now loop throgh all values and print results
for i in ${qDIMS[@]}; do
	# for j in ${rDIMS[@]}; do
		# create the sample data file
		python data.py $rows $i $i
		# now run algoritm on it to get time for each inputs
		time=`python sm_gs.py`
		echo $i$'\t'$i$'\t'$time
		echo $i$'\t'$i$'\t'$time >> dims1.txt
		# now run algoritm on it to get time for each inputs
		time=`python run.py`
		echo $i$'\t'$i$'\t'$time
		echo $i$'\t'$i$'\t'$time >> dims2.txt
	# done
done
echo 'Done for '$rows''

rows=2000

echo '----' >> dims1.txt
echo '----' >> dims2.txt

# now loop throgh all values and print results
for i in ${qDIMS[@]}; do
	# for j in ${rDIMS[@]}; do
		# create the sample data file
		python data.py $rows $i $i
		# now run algoritm on it to get time for each inputs
		time=`python sm_gs.py`
		echo $i$'\t'$i$'\t'$time
		echo $i$'\t'$i$'\t'$time >> dims1.txt
		# now run algoritm on it to get time for each inputs
		time=`python run.py`
		echo $i$'\t'$i$'\t'$time
		echo $i$'\t'$i$'\t'$time >> dims2.txt
	# done
done
echo 'Done for '$rows''

# echo R$'\t'T > rows1.txt
# echo R$'\t'T > rows2.txt

# q=${qDIMS[1]}
# r=${qDIMS[3]}

# for i in ${ROWS[@]}; do
# 	# create the sample data file
# 	python data.py $i $q $r
# 	# now run algoritm on it to get time for each inputs
# 	time=`python sm_gs.py`
# 	echo $i$'\t'$time
# 	echo $i$'\t'$time >> rows1.txt
# 	# now run algoritm on it to get time for each inputs
# 	time=`python run.py`
# 	echo $i$'\t'$time
# 	echo $i$'\t'$time >> rows2.txt
# done
