CS534 AI Project 1 (Search Methods)

1) Navigate to the Project Directory

TO RUN THE CODE:
  python search.py <graph_file_txt> <search_method>

  	There are nine search algorithms:
		depth_first
		breadth_first
		depth_limited
		depth_iterative
		uniform_cost
		greedy
		astar
		beam
		hillclimbing
	
	Example:
		python search.py graph.txt uniform_cost	

	NOTE: In order to run all searches, enter 'ALL' for <search algorithm>

   	      python search.py graph.txt ALL
			
 Sample Output for graph.txt ALL

 (1) Depth 1st Search 

 Expanded	Queue 
     S  	['S']
     A  	['AS', 'DS']
     B  	['BAS', 'DAS', 'DS']
     C  	['CBAS', 'EBAS', 'DAS', 'DS']
     E  	['EBAS', 'DAS', 'DS']
     D  	['DEBAS', 'FEBAS', 'DAS', 'DS']
     F  	['FEBAS', 'DAS', 'DS']
     G  	['GFEBAS', 'DAS', 'DS']
 Goal Reached!
 Goal Path:  SABEFG


 (2) Breadth 1st Search 

 Expanded	Queue 
     S  	['S']
     A  	['AS', 'DS']
     D  	['DS', 'BAS', 'DAS']
     B  	['BAS', 'DAS', 'ADS', 'EDS']
     D  	['DAS', 'ADS', 'EDS', 'CBAS', 'EBAS']
     A  	['ADS', 'EDS', 'CBAS', 'EBAS', 'EDAS']
     E  	['EDS', 'CBAS', 'EBAS', 'EDAS', 'BADS']
     C  	['CBAS', 'EBAS', 'EDAS', 'BADS', 'BEDS', 'FEDS']
     E  	['EBAS', 'EDAS', 'BADS', 'BEDS', 'FEDS']
     E  	['EDAS', 'BADS', 'BEDS', 'FEDS', 'DEBAS', 'FEBAS']
     B  	['BADS', 'BEDS', 'FEDS', 'DEBAS', 'FEBAS', 'BEDAS', 'FEDAS']
     B  	['BEDS', 'FEDS', 'DEBAS', 'FEBAS', 'BEDAS', 'FEDAS', 'CBADS', 'EBADS']
     F  	['FEDS', 'DEBAS', 'FEBAS', 'BEDAS', 'FEDAS', 'CBADS', 'EBADS', 'ABEDS', 'CBEDS']
     D  	['DEBAS', 'FEBAS', 'BEDAS', 'FEDAS', 'CBADS', 'EBADS', 'ABEDS', 'CBEDS', 'GFEDS']
     F  	['FEBAS', 'BEDAS', 'FEDAS', 'CBADS', 'EBADS', 'ABEDS', 'CBEDS', 'GFEDS']
     B  	['BEDAS', 'FEDAS', 'CBADS', 'EBADS', 'ABEDS', 'CBEDS', 'GFEDS', 'GFEBAS']
     F  	['FEDAS', 'CBADS', 'EBADS', 'ABEDS', 'CBEDS', 'GFEDS', 'GFEBAS', 'CBEDAS']
     C  	['CBADS', 'EBADS', 'ABEDS', 'CBEDS', 'GFEDS', 'GFEBAS', 'CBEDAS', 'GFEDAS']
     E  	['EBADS', 'ABEDS', 'CBEDS', 'GFEDS', 'GFEBAS', 'CBEDAS', 'GFEDAS']
     A  	['ABEDS', 'CBEDS', 'GFEDS', 'GFEBAS', 'CBEDAS', 'GFEDAS', 'FEBADS']
     C  	['CBEDS', 'GFEDS', 'GFEBAS', 'CBEDAS', 'GFEDAS', 'FEBADS']
     G  	['GFEDS', 'GFEBAS', 'CBEDAS', 'GFEDAS', 'FEBADS']
 Goal Reached!
 Goal Path:  SDEFG


 (3) Depth-Limted Search (Depth Limit = 2) 

 Expanded	Queue 
     S  	['S']
     A  	['AS', 'DS']
     B  	['BAS', 'DAS', 'DS']
     D  	['DAS', 'DS']
     D  	['DS']
     A  	['ADS', 'EDS']
     E  	['EDS']
 Failure to find path between S and G

 (4) Iterative Deepening Search

 L = 0
 Expanded	Queue 
     S  	['S']
 Failure to find path between S and G

 L = 1
 Expanded	Queue 
     S  	['S']
     A  	['AS', 'DS']
     D  	['DS']
 Failure to find path between S and G

 L = 2
 Expanded	Queue 
     S  	['S']
     A  	['AS', 'DS']
     B  	['BAS', 'DAS', 'DS']
     D  	['DAS', 'DS']
     D  	['DS']
     A  	['ADS', 'EDS']
     E  	['EDS']
 Failure to find path between S and G

 L = 3
 Expanded	Queue 
     S  	['S']
     A  	['AS', 'DS']
     B  	['BAS', 'DAS', 'DS']
     C  	['CBAS', 'EBAS', 'DAS', 'DS']
     E  	['EBAS', 'DAS', 'DS']
     D  	['DAS', 'DS']
     E  	['EDAS', 'DS']
     D  	['DS']
     A  	['ADS', 'EDS']
     B  	['BADS', 'EDS']
     E  	['EDS']
     B  	['BEDS', 'FEDS']
     F  	['FEDS']
 Failure to find path between S and G

 L = 4
 Expanded	Queue 
     S  	['S']
     A  	['AS', 'DS']
     B  	['BAS', 'DAS', 'DS']
     C  	['CBAS', 'EBAS', 'DAS', 'DS']
     E  	['EBAS', 'DAS', 'DS']
     D  	['DEBAS', 'FEBAS', 'DAS', 'DS']
     F  	['FEBAS', 'DAS', 'DS']
     D  	['DAS', 'DS']
     E  	['EDAS', 'DS']
     B  	['BEDAS', 'FEDAS', 'DS']
     F  	['FEDAS', 'DS']
     D  	['DS']
     A  	['ADS', 'EDS']
     B  	['BADS', 'EDS']
     C  	['CBADS', 'EBADS', 'EDS']
     E  	['EBADS', 'EDS']
     E  	['EDS']
     B  	['BEDS', 'FEDS']
     A  	['ABEDS', 'CBEDS', 'FEDS']
     C  	['CBEDS', 'FEDS']
     F  	['FEDS']
     G  	['GFEDS']
 Goal Reached!
 Goal Path:  SDEFG


 (5) Uniform Cost Search 

 Expanded	Queue 
     S  	[(0.0, 'S')]
     A  	[(3.0, 'AS'), (4.0, 'DS')]
     D  	[(4.0, 'DS'), (7.0, 'BAS'), (8.0, 'DAS')]
     E  	[(6.0, 'EDS'), (7.0, 'BAS'), (8.0, 'DAS'), (9.0, 'ADS')]
     B  	[(7.0, 'BAS'), (8.0, 'DAS'), (9.0, 'ADS'), (10.0, 'FEDS'), (11.0, 'BEDS')]
     D  	[(8.0, 'DAS'), (9.0, 'ADS'), (10.0, 'FEDS'), (11.0, 'BEDS'), (11.0, 'CBAS'), (12.0, 'EBAS')]
     A  	[(9.0, 'ADS'), (10.0, 'EDAS'), (10.0, 'FEDS'), (11.0, 'BEDS'), (11.0, 'CBAS'), (12.0, 'EBAS')]
     E  	[(10.0, 'EDAS'), (10.0, 'FEDS'), (11.0, 'BEDS'), (11.0, 'CBAS'), (12.0, 'EBAS'), (13.0, 'BADS')]
     F  	[(10.0, 'FEDS'), (11.0, 'BEDS'), (11.0, 'CBAS'), (12.0, 'EBAS'), (13.0, 'BADS'), (14.0, 'FEDAS'), (15.0, 'BEDAS')]
     B  	[(11.0, 'BEDS'), (11.0, 'CBAS'), (12.0, 'EBAS'), (13.0, 'BADS'), (13.0, 'GFEDS'), (14.0, 'FEDAS'), (15.0, 'BEDAS')]
     C  	[(11.0, 'CBAS'), (12.0, 'EBAS'), (13.0, 'BADS'), (13.0, 'GFEDS'), (14.0, 'FEDAS'), (15.0, 'ABEDS'), (15.0, 'BEDAS'), (15.0, 'CBEDS')]
     E  	[(12.0, 'EBAS'), (13.0, 'BADS'), (13.0, 'GFEDS'), (14.0, 'FEDAS'), (15.0, 'ABEDS'), (15.0, 'BEDAS'), (15.0, 'CBEDS')]
     B  	[(13.0, 'BADS'), (13.0, 'GFEDS'), (14.0, 'DEBAS'), (14.0, 'FEDAS'), (15.0, 'ABEDS'), (15.0, 'BEDAS'), (15.0, 'CBEDS'), (16.0, 'FEBAS')]
     G  	[(13.0, 'GFEDS'), (14.0, 'DEBAS'), (14.0, 'FEDAS'), (15.0, 'ABEDS'), (15.0, 'BEDAS'), (15.0, 'CBEDS'), (16.0, 'FEBAS'), (17.0, 'CBADS'), (18.0, 'EBADS')]
 Goal Reached!
 Goal Path:  SDEFG


 (6) Greedy Search 

 Expanded	Queue 
     S  	[(11.0, 'S')]
     D  	[(8.9, 'DS'), (10.4, 'AS')]
     E  	[(6.9, 'EDS'), (10.4, 'AS'), (10.4, 'ADS')]
     F  	[(3.0, 'FEDS'), (6.7, 'BEDS'), (10.4, 'AS'), (10.4, 'ADS')]
     G  	[(0.0, 'GFEDS'), (6.7, 'BEDS'), (10.4, 'AS'), (10.4, 'ADS')]
 Goal Reached!
 Goal Path:  SDEFG


 (7) A* Search 

 Expanded	Queue 
     S  	[(11.0, 'S')]
     D  	[(12.9, 'DS'), (13.4, 'AS')]
     E  	[(12.9, 'EDS'), (13.4, 'AS')]
     F  	[(13.0, 'FEDS'), (13.4, 'AS'), (17.7, 'BEDS')]
     G  	[(13.0, 'GFEDS'), (13.4, 'AS'), (17.7, 'BEDS')]
 Goal Reached!
 Goal Path:  SDEFG


 (8) Beam Search (w = 2)

 Expanded	Queue 
     S  	[(11.0, 'S')]
     A  	[(10.4, 'AS'), (8.9, 'DS')]
     D  	[(8.9, 'DS'), (6.7, 'BAS'), (8.9, 'DAS')]
     B  	[(6.7, 'BAS'), (6.9, 'EDS')]
     E  	[(6.9, 'EDS'), (4.0, 'CBAS'), (6.9, 'EBAS')]
     C  	[(4.0, 'CBAS'), (3.0, 'FEDS')]
     F  	[(3.0, 'FEDS')]
     G  	[(0.0, 'GFEDS')]
 Goal Reached!
 Goal Path:  SDEFG


 (9) HillClimbing Search 

 Expanded	Queue 
     S  	[(11.0, 'S')]
     D  	[(8.9, 'DS')]
     E  	[(6.9, 'EDS')]
     F  	[(3.0, 'FEDS')]
     G  	[(0.0, 'GFEDS')]
 Goal Reached!
 Goal Path:  SDEFG

