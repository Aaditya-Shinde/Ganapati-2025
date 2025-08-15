import time
import actions
import patterns

try:
    actions.setup()
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

        print("\n\n\n***********Shifted***********")

except Exception as e:
    print("\n\n\n"+'*'*25+"EXCEPTION"+'*'*25)
    print(e)
    print('*'*50)
finally:
    actions.cleanup()