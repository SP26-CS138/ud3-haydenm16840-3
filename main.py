'''
DEVELOPER(S): Hayden Montgomery
COLLABORATORS: 
DATE: 4/3/26
'''

"""
This is a statistics program used to automatically calculate mean, variance, and the z-score when given a dataset.

Leave one blank line.  The rest of this docstring should contain an
overall description of the program.
"""

##########################################
# IMPORTS:
#   Math module is imported to utilize the math.sqrt() function.
##########################################
import math

##########################################
# FUNCTIONS:
##########################################
def compute_sample_mean(formatted_data): #Works as intended
    '''Computes the sample mean of both file input or manual input.'''
    total_data_values = 0
    for i in range(len(formatted_data)):
        total_data_values += formatted_data[i]
    
    total_data_values = total_data_values / len(formatted_data)

    return total_data_values


def compute_sample_variance(formatted_data, sample_mean): #Works as intended
    '''Computes sample variance'''
    summed_deviations = 0
    temp = formatted_data.copy() #Changing the original list breaks the median calculations
    for i in range(len(temp)):
        temp[i] = (temp[i] - sample_mean) ** 2
        summed_deviations += temp[i]

    sample_variance = summed_deviations / (len(temp) - 1)

    return sample_variance


def compute_sample_median(formatted_data):
    '''Computes sample median'''
    sample_median = 0
    formatted_data.sort() #Needs to be from least to greatest

    if len(formatted_data) % 2 == 0: #EVEN
        value1 = formatted_data[(len(formatted_data) // 2) - 1]
        value2 = formatted_data[(len(formatted_data) // 2)] # + 1 = next value
       
        sample_median = (value1 + value2) / 2

        return sample_median 

    else:
        sample_median = formatted_data[len(formatted_data) // 2]
        
        return sample_median


def compute_standard_deviation(sample_variance):
    '''Calculates standard deviation'''
    standard_deviation = math.sqrt(sample_variance)

    return standard_deviation


def compute_zscores(formatted_data, sample_mean, standard_deviation ):
    '''Calcaultes z-scores and returns as a list'''
    zscores = formatted_data.copy()
    
    if standard_deviation != 0: 
        for i in range(len(zscores)):
            zscores[i] = (zscores[i] - sample_mean) / standard_deviation

    else: #If the standard deviation is 0 that means the above loop will be dividing by 0 which would break the program, so the else sets the z-scores to 0
        for i in range(len(zscores)):
            zscores[i] = 0

    return zscores


def get_inputfile(): #Works as intended
    '''Asks for the input file and validates that it exists (until the user enters a valid file)'''
    while True:
        file_name = str(input('\nEnter the name of the file you would like to read from: '))       
        file_name += '.txt' #It's annoying to have to type .txt for every entry.

        try:
            #Testing to see if file exists
            file = open(file_name, 'r')
            
            #Storing file as a string in user_data
            user_data = file.read()
            
            #Closing file to save resources
            file.close()
            
            return user_data
        
        except FileNotFoundError:
            print('\nThe file entered was not found, please ensure that the file exists!\n')


def manual_user_input(): #Works as intended
    '''Lets the user manually enter in their data values if a file doesn't exist.'''
    formatted_data = []
    while True:
        user_input = input('Please enter your data values and type @ when finished: ')

        if user_input == '@':
            if len(formatted_data) == 0:
                print('At least one value must be entered for the calculations!')
            
            else:
                print('Input Complete!')
                break
        
        else:
            try:
                formatted_data.append(float(user_input))

            except ValueError:
                print('Invalid input, please try again or @ to stop: ')

    return formatted_data


def format_user_data(user_data): #Works as intended, ONLY FOR FILE INPUT
    '''Splits user's data by commas so that a list can be used for calculations'''
    formatted_data = user_data.split(',')
    for i in range(len(formatted_data)):
        formatted_data[i] = formatted_data[i].strip() 
        formatted_data[i] = float(formatted_data[i])

    return formatted_data


def output_user_calcs_term():
    '''Formats and outputs user's calculations in the terminal'''
    term_outupt = ''
    

def output_user_calcs_file():
    '''Formats and outputs user's calculations as a .txt'''


##########################################
# MAIN PROGRAM:
##########################################
def main():
    print('\n--------------------------\nBasic Economics Calculator\n--------------------------\n')
    user_input1 = str(input('Calculate with File (F) or Manual Input (M): ')).upper()
    while True:
        if user_input1 == 'F':
            user_data = get_inputfile() #Getting user data
            formatted_data = format_user_data(user_data) #Formatting user data for calculations
            break

        elif user_input1 == 'M':
            user_data = manual_user_input() #Getting user data (already formatted)
            break
        
        else: 
            print('\nInvalid choice, please try again: \n')
            user_input1 = str(input('Calculate with File (F) or Manual Input (M): ')).upper()

    sample_mean = compute_sample_mean(formatted_data)
    sample_variance = compute_sample_variance(formatted_data, sample_mean)
    sample_median = compute_sample_median(formatted_data)
    standard_deviation = compute_standard_deviation(sample_variance)
    zscores = compute_zscores(formatted_data, sample_mean, standard_deviation)

    user_input2 = str(input('\nOuput as File (F) or to Terminal (T): ')).upper()
    
    #while True:



if __name__ == "__main__":
    main()
