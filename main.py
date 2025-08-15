import time
import actions
import patterns

try:
    print("*******All turned OFF********")
    while True:
        actions.send_pattern(patterns.pattern_0)
        time.sleep(0.3)
        
        actions.send_pattern(patterns.pattern_1)
        time.sleep(0.3)
        
        actions.send_pattern(patterns.pattern_2)
        time.sleep(0.3)
        
        actions.send_pattern(patterns.pattern_3)
        time.sleep(0.3)
        
        actions.send_pattern(patterns.pattern_4)
        time.sleep(0.3)

        print("***********Shifted***********")

except Exception as e:
    print('*'*50)
    print(e)
    print('*'*50)
finally:
    actions.cleanup()