from home_module import *

show_menu()
home=get_home_data()
home_list=[home]
show_home_list(home_list)
address=input("Enter address:")
result=find_home_by_address(home_list,address)
if result is not None:
    print("Address Found")
else:
    print("Address Not Found")
