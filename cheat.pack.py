def cheat(question = None):
    if question == "Q2.2P.1":
        print("""
        # ------------------------------------------- Q2.2P.1
        
        current_hour = datetime.datetime.now().hour
        current_minute = datetime.datetime.now().minute
        current_time = int(str(current_hour)+str(current_minute))
        
        print("The current time is:", current_time)
        if current_time >= 100 and current_time < 400:
            print("Go to sleep!")
        elif current_time >= 800 and current_time < 900:
            print("Eet je hagelslag!")
        else:
            print("Gut gemacht!")
        """)

    elif question == "Q2.2P.2":
        print("""
        # ------------------------------------------- Q2.2P.2
        
        numeric_vec = np.random.uniform(low=0, high=100, size=4)
        
        weight_sum = 0
        for i in range(len(numeric_vec)):
            if (i+1) % 2 == 0:
                weight_sum = weight_sum + 2*numeric_vec[i]
            else:
                weight_sum = weight_sum + numeric_vec[i]
        
        weight_avg = weight_sum / (np.size(numeric_vec)*1.5)
        
        """)

    elif question == "Q2.2P.3":
        print("""
        # ------------------------------------------- Q2.2P.3
        
        # -------------------- Q2.2P.3a
        
        # No, this code does not run in Python.
        # and we get the following error:
        # UnboundLocalError: local variable grass referenced before assignment
        
        # This is different to R (where it ran).
        
        # Because a local variable grass is defined in the third line of the function
        # Python thinks that by using grass in the first line of the function
        # we do not mean the global variable but the one defined later on.
        # Since the latter is only defined later one,
        # using it in the first line to assign a value to grass_me is not possible
        
        
        # -------------------- Q2.2P.3b
        
        grass = "green"
        def color_it(color_me, grass_me):
            color_me = "blue"
            grass_me = grass # we could also assign "grass" here to make it not reliant on the global variable
            colorful_items = np.array([(color_me, grass_me)])
            return colorful_items
        
        sky = "grey"
        ground = "brown"
        these_items = color_it(sky, ground)
        print(these_items)
        """)

    elif question == "Q2.2P.4":
        print("""
        # ------------------------------------------- Q2.2P.4
        
        # -------------------- Q2.2P.4a
        
        vec1 = np.array([1, 2, 2, 2, 4, -99.1])
        
        def special(input_vector):
            duplicates = np.array([])
            output_vector = np.array([])
            for i in input_vector:
                occurrences = 0
                for j in input_vector: # first we count the number of times an element is in the list
                    if i == j:
                        occurrences = occurrences + 1
                if occurrences == 1: # if value is unique is is just appended to output
                    output_vector = np.append(output_vector, i)
                else:
                    if i not in duplicates: # otherwise, if not already in duplicates, its also added to output
                        duplicates = np.append(duplicates, i)
                        output_vector = np.append(output_vector, i)
        
            int_counter = 0 # check if only ints in input_vector
            for i in input_vector:
                if i == round(i):
                    int_counter = int_counter + 1
            if int_counter == len(input_vector): # if there are only ints, then convert output to ints
                output_vector = output_vector.astype(int) # in order to match format of unique() output
            return(output_vector)
        
        print(vec1)
        print(np.unique(vec1))
        print(special(vec1))
        
        
        # -------------------- Q2.2P.4b
        
        def special(input_vector):
        
            if isinstance(input_vector, np.ndarray) == False:
                raise Exception("Sorry, only Numpy vectors allowed.")
        
            duplicates = np.array([])
            output_vector = np.array([])
            for i in input_vector:
                occurrences = 0
                for j in input_vector: # first we count the number of times an element is in the list
                    if i == j:
                        occurrences = occurrences + 1
                if occurrences == 1: # if value is unique is is just appended to output
                    output_vector = np.append(output_vector, i)
                else:
                    if i not in duplicates: # otherwise, if not already in duplicates, its also added to output
                        duplicates = np.append(duplicates, i)
                        output_vector = np.append(output_vector, i)
        
            int_counter = 0 # check if only ints in input_vector
            for i in input_vector:
                if i == round(i):
                    int_counter = int_counter + 1
            if int_counter == len(input_vector): # if there are only ints, then convert output to ints
                output_vector = output_vector.astype(int) # in order to match format of unique() output
            return(output_vector)
        
        print(vec1)
        print(np.unique(vec1))
        print(special(vec1))
        # print(special("hello")) # worked (gave error) if I ran this code line here
        """)

    else:
        print("This function only works for Q2.2P.1 to Q2.2P.4")