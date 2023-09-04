# from controller.customer_controller import CustomerController
from controller.contract_controller import ContractController
# from model.entity.contract import Contract
from controller.boarding_controller import BoardingController
# from model.da.utills.boarding_da import BoardingDa
# from controller.rewarding_controller import RewardingController
# from model.da.utills.customer_da import CustomerDa

#customer test
# print(CustomerController.save("دیده بان سازه نور", "10320782872", "12114"))
# print(CustomerController.check_code_exist(4))
# print(CustomerController.remove(4))

# CustomerController.save("پارسیان", 10320880884, 31973, "ساختمان", 1)
# CustomerController.edit(5, "پارسیان", "10320880784", "31974", "ساختمان", 1)
# print(CustomerController.check_code_exist("2"))
# print(cu.check_score("نفت و گاز", 5))
# CustomerController.check_code_exist(2)


# contract test
print(ContractController.save("لاهیجان", "ساختمان", 1394, 1396, 40692))
# print(ContractController.edit(4, "لاهیجان", "ساختمان", 1394, 1398, 40692))
# con = Contract(6, "ایلام", "راه", 1394, 1396, 40692)
# print(ContractController.check_contract_exist(con))
# print((ContractController.check_code_exists(6)))
# print(ContractController.edit(2, "ایلام", "کشاورزی", 1398, 1402, 8451664455))
# print(ContractController.edit(6, "ایلام", "کشاورزی", 1398, 1402, 8451664455))
# print(ContractController.save("اهواز", "راه", 1401, 1401, 64487655))
# print(ContractController.edit(4,"اهواز", "راه", 1401, 1401, 64487655))
# print(ContractController.save("اهواز", "راه", 1401, 1401, 64487655))
# print(ContractController.remove(1))
# print(ContractController.remove(1))
# print(ContractController.find_all())
# print(ContractController.find_by_start_year(1398, 1405))
# print(ContractController.find_by_price_range(0,89511454646))
# print(ContractController.find_by_end_year(1402,1402))
# print(ContractController.find_by_subject("راه"))



#boarding test
# print(BoardingController.save("علی", "ماضی", "0023541605", "کارشناسی", "معماری", 15))
# print(BoardingController.remove(4))
# print(BoardingController.edit(2, "علی", "رمضانی", "0023541605", "کارشناسی", "معماری", 5))
# print(BoardingController.find_all())
# print(BoardingController.find_by_name("ALI"))
# print(BoardingController.save("علی", "رضوانی", "0023541605", "کارشناسی", "معماری", 17))
# print(BoardingController.edit(6, "علی", "رمضانی", "0023541605", "کارشناسی ارشد", "معماری", 5))
# print(BoardingController.remove(2))
# print(BoardingController.find_all())

#rewarding test
# print(RewardingController.save("علی", "علیجانی", "0023541605", "کارشناسی", "معماری", 5))
# # print(RewardingController.edit(1, "علی", "رمضانی", "0023541605", "کارشناسی", "معماری", 5))
# print(RewardingController.edit(3, "علی", "رمضانی", "0023541605", "فوق دیپلم", "معماری", 5))
# print(RewardingController.save("علی", "رضوانی", "0023541605", "کارشناسی", "عمران", 10))
