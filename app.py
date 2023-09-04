from flask import Flask, render_template, request, flash, redirect, url_for
import secrets
from controller.boarding_controller import BoardingController
from controller.rewarding_controller import RewardingController
from controller.contract_controller import ContractController
from controller.customer_controller import CustomerController
from controller.makedb_controller import MakeDbController


app = Flask(__name__, template_folder="view", static_folder="view/assets")
app.secret_key = secrets.token_hex(16)

def common_logic():
    success1, contract_list = ContractController.find_all()
    success2, contract_sum = ContractController.calc_sum_score()

    success3, boarding_list = BoardingController.find_all()
    success4, boarding_sum = BoardingController.calc_sum_score()

    success5, rewarding_list = RewardingController.find_all()
    success6, rewarding_sum = RewardingController.calc_sum_score()

    return contract_list, contract_sum[0], boarding_list, boarding_sum[0], rewarding_list, rewarding_sum[0]

def show_customer_indicator():
    customer_list = CustomerController.show_customer()
    name = customer_list[0][1]
    nation_code = customer_list[0][2]
    registration_code = customer_list[0][3]
    subject = customer_list[0][4]
    grade = customer_list[0][5]

    customer = {"name": name, "nation_code": nation_code, "registration_code": registration_code, "subject": subject,
                "grade": grade}
    contract_indicator, boarding_indicator, rewarding_indicator = CustomerController.show_indicator()
    return customer, boarding_indicator, rewarding_indicator, contract_indicator

@app.route("/")
def home():
    MakeDbController.make_db()
    return render_template("mainpage.html")

@app.route("/mainpage", methods=["GET"])
def show_main():
    return render_template("mainpage.html")


@app.route("/calculate", methods=["GET"])
def show_calculate():
    return render_template("calculate.html")

@app.route("/services", methods=["GET"])
def show_services():
    return render_template("services.html")

@app.route("/contactus", methods=["GET"])
def show_contactus():
    return render_template("contactus.html")

@app.route("/customerdata", methods=["GET"])
def show_customerdata():
    return render_template("customerdata.html")


@app.route("/go_to_calculate", methods=["POST"])
def go_to_calculate():
    name = request.form.get("name")
    nation_code = request.form.get("nation_code")
    registration_code = request.form.get("registration_code")
    subject = request.form.get("subject")
    grade = int(request.form.get("grade"))
    customer = {"name": name, "nation_code": nation_code, "registration_code": registration_code, "subject": subject, "grade": grade}

    success, message = CustomerController.save(name, nation_code, registration_code, subject, grade)

    if success:
        contract_indicator, boarding_indicator, rewarding_indicator = CustomerController.show_indicator()
        return render_template("calculate.html", customer=customer, contract_indicator=contract_indicator,
                               boarding_indicator=boarding_indicator, rewarding_indicator=rewarding_indicator)
    else:
        flash(f"Error: {message}", "error")
        return redirect(url_for("show_customerdata"))



@app.route("/save_boarding", methods=["POST"])

def save_boarding():
    success, message1 = BoardingController.save(request.form.get("name"), request.form.get("family"),
                            request.form.get("melli"), request.form.get("grade"),
                            request.form.get("major"), int(request.form.get("work_years")))

    contract_list, contract_sum, boarding_list, boarding_sum, rewarding_list, rewarding_sum = common_logic()
    customer, boarding_indicator, rewarding_indicator, contract_indicator = show_customer_indicator()

    return render_template("calculate.html", message1=message1, contract_list=contract_list, boarding_list=boarding_list,
            rewarding_list=rewarding_list, contract_sum=contract_sum,
            boarding_sum=boarding_sum, rewarding_sum=rewarding_sum,
            customer=customer, contract_indicator=contract_indicator,
            boarding_indicator=boarding_indicator, rewarding_indicator=rewarding_indicator)


@app.route("/save_personnel", methods=["POST"])
def save_personnel():
    success, message2 = RewardingController.save(request.form.get("name"), request.form.get("family"), request.form.get("melli"),
             request.form.get("grade"), request.form.get("major"), int(request.form.get("work_years")))

    contract_list, contract_sum, boarding_list, boarding_sum, rewarding_list, rewarding_sum = common_logic()
    customer, boarding_indicator, rewarding_indicator, contract_indicator = show_customer_indicator()

    return render_template("calculate.html",message2=message2, contract_list=contract_list, boarding_list=boarding_list,
                           rewarding_list=rewarding_list, contract_sum=contract_sum,
                           boarding_sum=boarding_sum, rewarding_sum=rewarding_sum, customer=customer, contract_indicator=contract_indicator, boarding_indicator=boarding_indicator, rewarding_indicator=rewarding_indicator)


@app.route("/save_contract", methods=["POST"])
def save_contract():
    success, message3 = ContractController.save(request.form.get("name"), request.form.get("subject"), int(request.form.get("start_year")), int(request.form.get("end_year")), int(request.form.get("price")))

    contract_list, contract_sum, boarding_list, boarding_sum, rewarding_list, rewarding_sum = common_logic()
    customer, boarding_indicator, rewarding_indicator, contract_indicator = show_customer_indicator()

    return render_template("calculate.html", message3=message3, contract_list=contract_list, boarding_list=boarding_list,
                           rewarding_list=rewarding_list, contract_sum=contract_sum,
                           boarding_sum=boarding_sum, rewarding_sum=rewarding_sum, customer=customer,
                           contract_indicator=contract_indicator, boarding_indicator=boarding_indicator,
                           rewarding_indicator=rewarding_indicator)


@app.route("/delete_customer", methods=["POST"])
def delete_customer():
    MakeDbController.make_db()
    return render_template("customerdata.html")


@app.route("/delete_boarding", methods=["POST"])
def delete_boarding():

    code = int(request.form.get("boarding_id"))
    print(BoardingController.remove(code))

    contract_list, contract_sum, boarding_list, boarding_sum, rewarding_list, rewarding_sum = common_logic()
    customer, boarding_indicator, rewarding_indicator, contract_indicator = show_customer_indicator()

    return render_template("calculate.html", contract_list=contract_list, boarding_list=boarding_list,
                           rewarding_list=rewarding_list, contract_sum=contract_sum,
                           boarding_sum=boarding_sum, rewarding_sum=rewarding_sum, customer=customer, contract_indicator=contract_indicator, boarding_indicator=boarding_indicator, rewarding_indicator=rewarding_indicator)


@app.route("/delete_rewarding", methods=["POST"])
def delete_rewarding():
    code = int(request.form.get("rewarding_id"))
    print(RewardingController.remove(code))

    contract_list, contract_sum, boarding_list, boarding_sum, rewarding_list, rewarding_sum = common_logic()
    customer, boarding_indicator, rewarding_indicator, contract_indicator = show_customer_indicator()

    return render_template("calculate.html", contract_list=contract_list, boarding_list=boarding_list,
                           rewarding_list=rewarding_list, contract_sum=contract_sum,
                           boarding_sum=boarding_sum, rewarding_sum=rewarding_sum, customer=customer,
                           contract_indicator=contract_indicator, boarding_indicator=boarding_indicator,
                           rewarding_indicator=rewarding_indicator)

@app.route("/delete_contract", methods=["POST"])
def delete_contract():
    code = int(request.form.get("contract_id"))
    print(ContractController.remove(code))

    contract_list, contract_sum, boarding_list, boarding_sum, rewarding_list, rewarding_sum = common_logic()
    customer, boarding_indicator, rewarding_indicator, contract_indicator = show_customer_indicator()

    return render_template("calculate.html", contract_list=contract_list, boarding_list=boarding_list,
                           rewarding_list=rewarding_list, contract_sum=contract_sum,
                           boarding_sum=boarding_sum, rewarding_sum=rewarding_sum, customer=customer,
                           contract_indicator=contract_indicator, boarding_indicator=boarding_indicator,
                           rewarding_indicator=rewarding_indicator)

app.run(host="127.0.0.1", port=80)
