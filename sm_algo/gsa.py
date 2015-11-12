#!/usr/bin/ python

class GSA():
	""" Gale-Shapley (Stable Marriage) Algorithm """
	def __init__(self, setA, setB):
		self.a = setA
		self.b = setB
		
	'''
	Algorithm to compute matched pairs 
	'''	


	def computePreferenceList1(self, person, opposite_list):
		score_list = []
		for i in range(0,len(opposite_list)):
			(id, score) = (opposite_list[i].child.id, sum([a*b for a,b in zip(person.child.data, opposite_list[i].mbr.minDim)]))
			score_list.append((id, score))
		return sorted(score_list,reverse=True,key=lambda x: x[1])


	def computePreferenceList2(self, person, opposite_list):
		score_list = []
		for i in range(0,len(opposite_list)):
			score = sum([a*b for a,b in zip(person.child.data, opposite_list[i].mbr.minDim)])
			score_list.append(score)
		return score_list

	def Marriage(self):
		# match will contain matched pair
		# matched = [ [from_set_a], [from_set_b] ]
		
		
		matched = []

		# unmatched will contain unmatched items from set b
		unmatched = []


		listA = []
		listB = []
		preference_listA = []
		preference_listB = []

		max_pairs = 0
		flag = 0
		# initially all women are not engaged to anyone
		if len(self.a) <= len(self.b):
			max_pairs = len(self.a)
			listA = self.a
			listB = self.b
		else:
			max_pairs = len(self.b)
			listA = self.b
			listB = self.a
			flag = 1

		for i in range(0,len(listA)):
			preference_listA.append(self.computePreferenceList1(listA[i],listB))
		for i in range(0,len(listB)):
			preference_listB.append(self.computePreferenceList2(listB[i],listA))

		partner_list = [(item.child.id,-1) for item in listB]

		# initially all are free
		engaged_listA = []

		pairs_made = 0

		while(pairs_made < max_pairs): # men are less 
			# find a free person
			free_person_index = -1
			for j in range(0,len(listA)):
				if not (j in engaged_listA):
					free_person_index = j
					break

			# find appropriate pair according to his/her preferences
			
			while len(preference_listA[free_person_index]) > 0:
				# if i in engaged_listA:
				# 	break

				# find a partner to which this person havn't yet proposed

				# check if partner is engaged

				# if it is, check for partners preference

				# if not, engange person with partner
				# print "------------"
				person_id,score = preference_listA[free_person_index][0]

				# now remove the proposed partner
				preference_listA[free_person_index].remove((person_id,score))
				
				partner = -1
				index = -1
				x = 0
				for y in partner_list:
				 	if y[0] == person_id:
				 		partner = y[1]
				 		index = x
				 		break
				 	x += 1

				# if partner is free, lets engage 
				if partner == -1:
					partner_list[index] = (person_id, free_person_index)
					engaged_listA.append(free_person_index)
					pairs_made += 1
					break

				# else engage only if preference allows it
				else:
					person_engaged = partner
					if preference_listB[index][person_engaged] < preference_listB[index][free_person_index]:
						partner_list[index] = (person_id, free_person_index)
						engaged_listA.append(free_person_index)
						engaged_listA.remove(person_engaged) 
						break


		# compute the match for set a and b
		"""
			for set a (for set b, just replace a with b)
		quality = self.a[i].mbr.minDim
			require = self.a[i].child.data
			id = self.a[i].child.id
		"""
		matchedA = []
		

		matchedB = []
		unmatchedB = []

		i = 0
		for item in partner_list:
			if item[1] != -1:
				matchedB.append(listB[i])
				matchedA.append(listA[item[1]])
			else:
				unmatchedB.append(listB[i])
			i += 1

		if flag == 0:
			matched.append(matchedA)
			matched.append(matchedB)
		else:
			matched.append(matchedB)
			matched.append(matchedA)
		unmatched.append(unmatchedB)
		
		# for now
		# if len(self.a) <= len(self.b):
		# 	matched.append(self.a)
		# 	matched.append(self.b[:len(self.a)])
		# 	unmatched = self.b[len(self.a):]
		# else:
		# 	matched.append(self.a[:len(self.b)])
		# 	matched.append(self.b)
		# 	unmatched = self.a[len(self.b):]

		return [matched, unmatched] 