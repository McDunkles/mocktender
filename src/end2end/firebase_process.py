from sensor_system_e2e import RPi_Node
from sense_hat import SenseHat

sense = SenseHat()

RUNNER = "rpi1"

def test_connectivity(name):
    rpi = RPi_Node(name)
    result = rpi.testConnectivity();
    return result

#RPi1 sends to RPi2
def test_case_1to2():
    rpi1 = RPi_Node("rpi1")
    rpi2 = RPi_Node("rpi2")
    send_result = rpi1.send_message("SEND_TEST1to2", rpi2)
    print("RPi1 Send Result = "+str(send_result))


#RPi2 receives from RPi1
def test_case_2from1():
    
    rpi2 = RPi_Node("rpi2")
    
    msg = rpi2.receive_message()
    print("RPi2 Message = "+str(msg))

def test_case_1to3():
    rpi1 = RPi_Node("rpi1");
    rpi3 = RPi_Node("rpi3");

    send_result = rpi1.send_message("SEND_TEST1to3", rpi3)
    print("RPi1 Send Result = " + str(send_result))

def test_case_3from1():
    rpi3 = RPi_Node("rpi3")

    msg = rpi3.receive_message()
    print("RP13 Message = "+str(msg))

def test_case_2to1():
    rpi1 = RPi_Node("rpi1")
    rpi2 = RPi_Node("rpi2")
    send_result = rpi2.send_message("SEND_TEST2to1", rpi1)
    print("RPi2 Send Result = "+str(send_result))

def test_case_1from2():
    rpi1 = RPi_Node("rpi1")

    msg = rpi1.receive_message()
    print("RPi2 Message = "+str(msg))

def test_case_3to1():
    rpi1 = RPi_Node("rpi1")
    rpi3 = RPi_Node("rpi3")
    send_result = rpi3.send_message("SEND_TEST3to1", rpi1)
    print("RPi3 Send Result = "+str(send_result))

def test_case_1from3():
    rpi1 = RPi_Node("rpi1")

    msg = rpi1.receive_message()
    print("RPi3 Message = "+str(msg))


def main():
    print("Hi")
    test_connectivity(RUNNER)
    if RUNNER == "rpi1":
        test_case_1to2()
        
if __name__ == '__main__':
    main()