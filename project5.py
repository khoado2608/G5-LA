import pandas as pd 
import numpy as np 

def savetocsv(matrix,filename):
	df = pd.DataFrame(matrix)
	df.to_csv(filename, index = False, header = False)

# task 1.1
scores_data = pd.read_csv('D:\\HCMUT-K23\\HK232\\Linear Algebra\\BTL\\material for BTL\\datascores.csv', header=None)
differentials_data = pd.read_csv('D:\\HCMUT-K23\\HK232\\Linear Algebra\\BTL\\material for BTL\\datadifferentials.csv', header=None)

# task 1.2
# Convert DataFrame to numpy arrays
games = np.abs(scores_data.values)
total = np.sum(games,axis=1)
RS = np.sum(scores_data,axis = 1)
# Calculate Colley Matrix
ColleyMatrix = 2 * np.eye(10) + np.diag(total.flatten()) - games #dung lenh flatten du lieu cua total
RightSide = (1 + 0.5 * RS)

#task 1.3
RanksColley = np.linalg.solve(ColleyMatrix, RightSide) #ColleyMatrix * RanksColley = RightSide => Ax=b => tim x
def sorting(rank,team):
     lst = pd.DataFrame({'Ranks':np.ravel(rank), 'Teams':team})
     lst_sorted = lst.sort_values(by='Ranks', ascending = False)
     lst_sorted['Ranks'] = lst_sorted['Ranks'].round(3)
     return lst_sorted

#task 1.4
Teams = ['Baylor', 'Iowa State', 'University of Kansas', 'Kansas State', 'University of Oklahoma', 'Oklahoma State', 'Texas Christian', 'University of Texas Austin', 'Texas Tech', 'West Virginia']
Ranking = sorting(RanksColley,Teams)

#Task 1.5
P = pd.DataFrame(columns=range(10))
B = pd.Series(dtype=float)
for i in range(10):
    for j in range(i + 1, 10):
        value = differentials_data.iloc[i, j]
        if value != 0:
            # Create a DataFrame containing data for each pair of teams
            data = pd.DataFrame([[1, -1]], columns=[i, j])
            # Concatenate the DataFrame to P
            P = pd.concat([P, data], ignore_index=True)
            # Append the value to B
            B = pd.concat([B, pd.Series(value)], ignore_index=True)
# Reset the index of P
P.reset_index(drop=True, inplace=True)
P.fillna(0, inplace=True)

#Task 1.6
P_trans = np.transpose(P)
B_trans = np.transpose(B)
A = pd.DataFrame(np.dot(P_trans, P))
D = pd.DataFrame(np.dot(P_trans, B_trans))

#Task 1.7
A.iloc[9, :] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
D.iloc[9, :] = 0
#task 1.8
RanksMassey = np.linalg.solve(A,D)

#Task 1.9
task19 = sorting(RanksMassey,Teams)

#Task 1.11, 1.12
def swapping(rank,teams):
    top_teams = rank.tolist()
    temp = top_teams[0]
    top_teams[0] = top_teams[1]
    top_teams[1] = temp
    rank = top_teams
    rounded_rank = [round(value, 3) for value in rank]
    return sorting(rank,teams)

task_111 = swapping(RanksColley,Teams)
task_112 = swapping(RanksMassey,Teams)

#lenh thuc thi file

# savetocsv(Ranking,'Task1_4.csv')
# savetcsv(task19, 'Task 1_9.csv')
# savetocsv(task_111, 'Task_111.csv')
# savetocsv(task_112, 'Task_112.csv')