import json

avg_salary_dict = {}


def count_avg_salary():
    with open("departments.json", 'r') as file:
        file_contents = json.load(file)
        
        assert file_contents != '' , "File is empty."
        
        for dep, salary in file_contents.items():
            avg_salary = sum(salary) / len(salary)
            avg_salary_dict[dep] = avg_salary
            
        
        
def main():
    try:
        count_avg_salary()
        with open("average_salary.json", "w") as file:
            json.dump(avg_salary_dict, file, indent = 4)
    except AssertionError as e:
        print("File is empty")
        
if __name__ == "__main__":
    main()
    