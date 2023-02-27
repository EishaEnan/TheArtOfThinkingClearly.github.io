#This script stores all the chapters as a 2D list  with chapter name as a string 
#and the refernces of chapters that its connected to in a list -> int

chapters = [['Survivorship Bias', [45, 49, 28, 31, 26, 94, 98]], 
            ["Swimmer's Body Illusion", [38, 20, 47, 71, 36]], 
            ['Clustering Illusion', [17, 24, 37]], 
            ['Social Proof', [25, 33, 79, 77]], 
            ['Sunk Cost Fallacy', [12, 68, 23, 60, 32, 20]], 
            ['Reciprocity', [42, 18, 22, 56]], 
            ['Confirmation Bias-1', [11, 95, 24, 64, 88]], 
            ['Confirmation Bias-2', [67, 83, 50, 80, 64, 99]], 
            ['Authority Bias', [57, 16, 40, 94]], 
            ['Contrast Effect', [11, 23, 38, 72, 19, 27, 42]], 
            ['Availability Bias', [80, 88, 48, 95, 7, 8, 10, 26]], 
            ["The It'll-Get-Worse-Before-It-Gets-Better Fallacy", [43, 5, 19]], 
            ['Story Bias', [37, 52, 87, 14, 36, 41, 78, 96, 99]], 
            ['Hindsight Bias', [97, 78, 13, 40, 20, 45]], 
            ['Overconfidence Effect', [94, 40, 89, 18, 45]], 
            ['Chauffeur Knowledge', [9, 76, 57]], 
            ['Illusion Of Control', [24, 26, 40, 94, 3, 67]], 
            ['Incentive Super-Response Tendency', [56, 6, 15]], 
            ['Regression To Mean', [55, 10, 12, 24, 29]]
            ['Outcome Bias', [5, 2, 14, 94]],
            ['The Paradox of Choice', [53, 71, 81]],
            ['Liking Bias', [6, 87]],
            ['Endowment Effect', [84, 5, 35, 10, 32, 50, 74, 82]],
            ['Coincidence', [37, 7, 8, 19, 17, 3]],
            ['Groupthink', [4, 33, 79, 91]],
            ['Neglect of Probability', [11, 28, 55, 1, 17, 34, 80]],
            ['Scarcity Error', [10, 82, 84]],
            ['Base-Rate Neglect', [1, 26, 29, 41, 55, 59, 80]],
            ["Gambler's Fallacy", [55, 28, 92, 19, 63]],
            ['The Anchor', [42]],
            ['Induction', [37, 1]],
            ['Loss Aversion', [84, 23, 33, 81, 5, 42, 66]],
            ['Social Loafing', [56, 4, 25, 32]],
            ['Exponential Growth', [63, 26, 61]],
            ["Winner's Curse", [23]],
            ['Fundamental Attribution Error', [13, 2, 83, 99, 38, 97]],
            ['False Casualty', [24, 48, 3, 13, 31, 49]],
            ['Halo Effect', [36, 83, 2, 10, 62]],
            ['Alternative Paths', [75, 80, 82, 47]],
            ['Forecast Illusion', [62, 91, 9, 14, 15, 17, 46, 75]],
            ['Conjunction Fallacy', [28, 13]],
            ['Framing', [10, 82, 32, 6, 30, 70]],
            ['Action Bias', [44, 90, 85, 12, 68]],
            ['Omission Bias', [65, 43, 85]],
            ['Self-Serving Bias', [14, 15, 74, 1, 49, 50, 64, 67, 96]],
            ['Hedonic Treadmill', [40, 69, 86]],
            ['Self-Selection Bias', [39, 95, 2]],
            ['Association Bias', [54, 37, 49, 11, 66]],
            ["Beginner's Luck", [1, 45, 48, 37, 94]],
            ['Cognitive Dissonance', [23, 45, 7, 8, 52, 60]],
            ['Hyperbolic Discounting', [53, 63, 85]],
            ["'Because' Justification", [50, 13, 97]],
            ['Decision Fatigue', [21, 51, 63, 81]],
            ['Contagion Bias', [48, 66]],
            ['The Problem with Averages', [28, 63, 19, 26, 29]],
            ['Motivation Crowding', [18, 6, 22]],
            ['Twaddle Tendency', [9, 76, 16]],
            ['Will Rogers Phenomenon', [98, 61]],
            ['Information Bias', [90, 99, 28]],
            ['Effort Justification', [5, 50]],
            ['The Law of Small Numbers', [34, 58]],
            ['Expectations', [75, 40, 38]],
            ['Simple Logic', [51, 53, 34, 29, 55]],
            ['Forer Effect', [95, 7, 8, 45]],
            ["Volunteer's Folly", [92, 44]],
            ['Affect Heuristic', [48, 32, 83, 54]],
            ['Introspection Illusion', [17, 45, 7, 8, 74]],
            ['Inability to Close Doors', [5, 43]],
            ['Neomania', [46]],
            ['Sleeper Effect', [42, 73, 99]],
            ['Alternative Bias', [21, 2]], 
            ['Social Comparison Bias', [86, 10]],
            ['Primacy and Recency Effects', [88, 70, 83]],
            ['Not-Invented-Here Syndrome', [67, 23, 45, 77]],
            ['The Black Swan', [80, 40, 39, 62]],
            ['Domain Dependence', [92, 16, 57]],
            ['False-Consensus Effect', [4, 74]],
            ['Falsification of History', [14, 13, 97]],
            ['In-Group Out-Group Bias', [4, 25]],
            ['Ambiguity Aversion', [75, 26, 28, 11, 39]],
            ['Default Effect', [53, 21, 32]],
            ['Fear Of Regret', [27, 23, 39, 42]],
            ['Salience Effect', [38, 73, 7, 8, 31, 36, 66]],
            ['House-Money Effect', [23, 27, 32]],
            ['Procastination', [44, 91, 43, 51, 93]],
            ['Envy', [72, 46]],
            ['Personification', [13, 99, 22]],
            ['Illusion of Attention', [95, 7, 8, 11, 73]],
            ['Strategic Misrepresentation', [15]],
            ['Overthinking', [43, 59]],
            ['Planning Fallacy', [85, 40, 93, 25]],
            ['Deformation Professionnelle', [65, 76, 29]],
            ['Zeigarnik Effect', [85, 91]],
            ['Illusion of Skill', [49, 1, 9, 15, 17, 20]],
            ['Feature-Positive Effect', [64, 7, 8, 47, 11, 88]],
            ['Cherry-picking', [13, 45]],
            ['Fallacy of the Single Cause', [52, 78, 14, 36]],
            ['Intention-To-Treat Error', [1, 58]],
            ['News Illusion', [36, 70, 7, 8, 59, 87, 13]]  
            ]