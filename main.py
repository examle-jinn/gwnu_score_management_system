from score_management_system import ScoreManagementSystem

if __name__ == "__main__":
    sms = ScoreManagementSystem() 
    sms.read('score.csv')
    print(sms.sort("avg", "des"))
    sms.write('result.csv', "avg", "des")