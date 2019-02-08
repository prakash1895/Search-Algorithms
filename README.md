# Search Algorithms
## CS534 AI HW1

1) Navigate to the Project Directory

TO RUN THE CODE:
  python search.py <graph_file_txt> <search_method>

  There are nine search algorithms:
	* depth_first
	* breadth_first
	* depth_limited
	* depth_iterative
	* uniform_cost
	* greedy
	* astar
	* beam
	* hillclimbing
	
Example:
       python search.py graph.txt uniform_cost	

NOTE: In order to run all searches, enter 'ALL' for <search algorithm>
      python search.py graph.txt ALL
	 
 (1) Depth 1st Search 

 Expanded	Queue 
     S  	['S']
     A  	['AS', 'MS']
     B  	['BAS', 'CAS', 'IAS', 'MS']
     C  	['CAS', 'IAS', 'MS']
     D  	['DCAS', 'ECAS', 'IAS', 'MS']
     E  	['ECAS', 'IAS', 'MS']
     I  	['IAS', 'MS']
     J  	['JIAS', 'MS']
     K  	['KJIAS', 'LJIAS', 'MS']
     L  	['LKJIAS', 'LJIAS', 'MS']
     M  	['MLKJIAS', 'LJIAS', 'MS']
     G  	['GMLKJIAS', 'LJIAS', 'MS']
 Goal Reached!
 Goal Path:  SAIJKLMG


 (2) Breadth 1st Search 

 Expanded	Queue 
     S  	['S']
     A  	['AS', 'MS']
     M  	['MS', 'BAS', 'CAS', 'IAS']
     B  	['BAS', 'CAS', 'IAS', 'GMS', 'LMS']
     C  	['CAS', 'IAS', 'GMS', 'LMS']
     I  	['IAS', 'GMS', 'LMS', 'DCAS', 'ECAS']
     G  	['GMS', 'LMS', 'DCAS', 'ECAS', 'JIAS']
 Goal Reached!
 Goal Path:  SMG


 (3) Depth-Limted Search (Depth Limit = 2) 

 Expanded	Queue 
     S  	['S']
     A  	['AS', 'MS']
     B  	['BAS', 'CAS', 'IAS', 'MS']
     C  	['CAS', 'IAS', 'MS']
     I  	['IAS', 'MS']
     M  	['MS']
     G  	['GMS', 'LMS']
 Goal Reached!
 Goal Path:  SMG


 (4) Iterative Deepening Search

 L = 0
 Expanded	Queue 
     S  	['S']
 Failure to find path between S and G

 L = 1
 Expanded	Queue 
     S  	['S']
     A  	['AS', 'MS']
     M  	['MS']
 Failure to find path between S and G

 L = 2
 Expanded	Queue 
     S  	['S']
     A  	['AS', 'MS']
     B  	['BAS', 'CAS', 'IAS', 'MS']
     C  	['CAS', 'IAS', 'MS']
     I  	['IAS', 'MS']
     M  	['MS']
     G  	['GMS', 'LMS']
 Goal Reached!
 Goal Path:  SMG


 (5) Uniform Cost Search 

 Expanded	Queue 
     S  	[(0.0, 'S')]
     A  	[(1.0, 'AS'), (15.0, 'MS')]
     C  	[(3.0, 'CAS'), (6.0, 'IAS'), (15.0, 'MS'), (51.0, 'BAS')]
     E  	[(4.0, 'ECAS'), (6.0, 'IAS'), (13.0, 'DCAS'), (15.0, 'MS'), (51.0, 'BAS')]
     I  	[(6.0, 'IAS'), (13.0, 'DCAS'), (15.0, 'MS'), (51.0, 'BAS')]
     J  	[(10.0, 'JIAS'), (13.0, 'DCAS'), (15.0, 'MS'), (51.0, 'BAS')]
     D  	[(13.0, 'DCAS'), (15.0, 'LJIAS'), (15.0, 'MS'), (51.0, 'BAS'), (60.0, 'KJIAS')]
     L  	[(15.0, 'LJIAS'), (15.0, 'MS'), (51.0, 'BAS'), (60.0, 'KJIAS')]
     M  	[(15.0, 'MS'), (20.0, 'KLJIAS'), (50.0, 'MLJIAS'), (51.0, 'BAS'), (60.0, 'KJIAS')]
     K  	[(20.0, 'KLJIAS'), (30.0, 'GMS'), (50.0, 'LMS'), (50.0, 'MLJIAS'), (51.0, 'BAS'), (60.0, 'KJIAS')]
     G  	[(30.0, 'GMS'), (50.0, 'LMS'), (50.0, 'MLJIAS'), (51.0, 'BAS'), (60.0, 'KJIAS')]
 Goal Reached!
 Goal Path:  SMG


 (6) Greedy Search 

 Expanded	Queue 
     S  	[(22.0, 'S')]
     A  	[(12.0, 'AS'), (14.0, 'MS')]
     I  	[(10.0, 'IAS'), (14.0, 'MS'), (16.0, 'CAS'), (24.0, 'BAS')]
     J  	[(8.0, 'JIAS'), (14.0, 'MS'), (16.0, 'CAS'), (24.0, 'BAS')]
     L  	[(4.0, 'LJIAS'), (6.0, 'KJIAS'), (14.0, 'MS'), (16.0, 'CAS'), (24.0, 'BAS')]
     K  	[(6.0, 'KJIAS'), (6.0, 'KLJIAS'), (14.0, 'MS'), (14.0, 'MLJIAS'), (16.0, 'CAS'), (24.0, 'BAS')]
     L  	[(4.0, 'LKJIAS'), (6.0, 'KLJIAS'), (14.0, 'MS'), (14.0, 'MLJIAS'), (16.0, 'CAS'), (24.0, 'BAS')]
     K  	[(6.0, 'KLJIAS'), (14.0, 'MLJIAS'), (14.0, 'MS'), (14.0, 'MLKJIAS'), (16.0, 'CAS'), (24.0, 'BAS')]
     M  	[(14.0, 'MLJIAS'), (14.0, 'MS'), (14.0, 'MLKJIAS'), (16.0, 'CAS'), (24.0, 'BAS')]
     G  	[(0.0, 'GMLJIAS'), (14.0, 'MS'), (14.0, 'MLKJIAS'), (16.0, 'CAS'), (24.0, 'BAS')]
 Goal Reached!
 Goal Path:  SAIJLMG


 (7) A* Search 

 Expanded	Queue 
     S  	[(22.0, 'S')]
     A  	[(13.0, 'AS'), (29.0, 'MS')]
     I  	[(16.0, 'IAS'), (19.0, 'CAS'), (29.0, 'MS'), (75.0, 'BAS')]
     J  	[(18.0, 'JIAS'), (19.0, 'CAS'), (29.0, 'MS'), (75.0, 'BAS')]
     C  	[(19.0, 'CAS'), (19.0, 'LJIAS'), (29.0, 'MS'), (66.0, 'KJIAS'), (75.0, 'BAS')]
     L  	[(19.0, 'LJIAS'), (22.0, 'ECAS'), (29.0, 'MS'), (33.0, 'DCAS'), (66.0, 'KJIAS'), (75.0, 'BAS')]
     E  	[(22.0, 'ECAS'), (26.0, 'KLJIAS'), (29.0, 'MS'), (33.0, 'DCAS'), (75.0, 'BAS')]
     K  	[(26.0, 'KLJIAS'), (29.0, 'MS'), (33.0, 'DCAS'), (75.0, 'BAS')]
     M  	[(29.0, 'MS'), (33.0, 'DCAS'), (75.0, 'BAS')]
     G  	[(30.0, 'GMS'), (33.0, 'DCAS'), (54.0, 'LMS'), (75.0, 'BAS')]
 Goal Reached!
 Goal Path:  SMG


 (8) Beam Search (w = 2)

 Expanded	Queue 
     S  	[(22.0, 'S')]
     A  	[(12.0, 'AS'), (14.0, 'MS')]
     M  	[(14.0, 'MS'), (24.0, 'BAS'), (16.0, 'CAS'), (10.0, 'IAS')]
     G  	[(0.0, 'GMS'), (4.0, 'LMS')]
 Goal Reached!
 Goal Path:  SMG


 (9) HillClimbing Search 

 Expanded	Queue 
     S  	[(22.0, 'S')]
     A  	[(12.0, 'AS')]
     I  	[(10.0, 'IAS')]
     J  	[(8.0, 'JIAS')]
     L  	[(4.0, 'LJIAS')]
     K  	[(6.0, 'KLJIAS')]
 Failure to find path between S and G
			
 
