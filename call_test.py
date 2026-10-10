from call_module import *

show_menu()
call=get_call_data()
call_list=[call]
show_call_list(call_list)
phone_number=int(input("Enter phone number: "))
result=find_call_by_phone_number(call_list,phone_number)
if result is not None:
    print("phone number Found")
else:
    print("phone number Not Found")
