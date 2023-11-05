import streamlit as st
import mysql.connector
from mysql.connector import Error
from streamlit_option_menu import option_menu
from datetime import datetime , time, timedelta
import pandas as pd
import matplotlib.pyplot as plt
from reportlab.pdfgen import canvas
import base64
from PIL import Image, UnidentifiedImageError
from io import BytesIO
import hydralit_components as hc


st.set_page_config(page_title="EMP PORTAL",
                   page_icon="https://hoabackgroundcheck.com/wp-content/uploads/2017/11/icon-Employees-Background-Check.png",
                   layout='wide', initial_sidebar_state='collapsed',)

hide_streamlit_style = '''
<style> #MainMenu{visibility:visible;}
footer{visibility:hidden;}
footer:after{
content:"Made By Shweta Dubey, Copyright @2023. All rights reserved";
font-size: medium;
text-align: center;
visibility: visible;
display:block;
background-color:hsla(0,100%,50%,0.3);
padding:0px;
top:0px;
}
</style>

'''
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


menu_data = [
    {'label':"Home"},
    {'label':"Employee"},
    {'label':"Employer"},
    {'label':"Feedback"},
]
over_theme = {'txc_inactive': '#F3F3F3'}
menu_id = hc.nav_bar(menu_definition=menu_data,
    override_theme= over_theme,
    hide_streamlit_markers=True, #will show the st hamburger as well as the navbar now!
    sticky_nav=False,#at the top or not
    sticky_mode='pinned') #jumpy or not-jumpy, but sticky or pinned


if menu_id =='Home':
    def add_bg_from_local(image_file):
        with open(image_file, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        st.markdown(
            f"""
        <style>
        .stApp {{
            background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
            background-size: cover
        }}
        </style>
        """,
            unsafe_allow_html=True
        )
    add_bg_from_local('C:/MyProject(ems)/ems/Scripts/images/emphome.png')

    col1, col2 = st.columns(2)
    with col1:
        image_path = "C:/MyProject(ems)/ems/Scripts/images/deck.png"

        with open(image_path, "rb") as f:
            image = f.read()


        style = """
            <style>
            .image-container {
                display: flex;
                justify-content: center;
                align-items: center;
                margin: -45px;
            }
            .image-container img {
                margin: 10px;
                max-width: 100%;
                max-height: 100%;
                height: 450px;
                width: 650px;
            }
            </style>
        """


        st.markdown(
            f'<div class="image-container">{style}'f'<img src="data:image/png;base64,{base64.b64encode(image).decode("utf-8")}" /></div>',
            unsafe_allow_html=True,
        )
        with col2:
            file_ = open("C:/MyProject(ems)/ems/Scripts/images/col.png", "rb")
            contents = file_.read()
            style = """
                        <style>
                        .image-container {
                            display: flex;
                            justify-content: center;
                            align-items: center;
                            margin: -45px;
                        }
                        .image-container img {
                            margin: 10px;
                            max-width: 100%;
                            max-height: 100%;
                            height: 450px;
                            width: 650px;
                        }
                        </style>
                    """


            st.markdown(
                f'<div class="image-container">{style}'f'<img src="data:image/png;base64,{base64.b64encode(contents).decode("utf-8")}" /></div>',
                unsafe_allow_html=True,
            )
    st.markdown("""
            <style>
            .highlight {
                color: #b26e08;
                text-align:left;
                padding: 5px;
                font-size: 45px;
            }
            </style>
            """, unsafe_allow_html=True)
    st.markdown('<h1 class="highlight">ABOUT', unsafe_allow_html=True)

    st.markdown(
        """
        <style>
        .about {
            color: #ffe1cd;
            text-align:left;
            border-radius: 5px;
            padding-bottom: 5px;
            padding-top: 0px;
            font-size: 23px;
            background-color: #bf3241;

        }
        </style>
        """, unsafe_allow_html=True)
    st.markdown(
        '<p class="about">It is a Web Application which manages the data of Employee And Employer, so that the features such as Time card entry ,Payroll data , About, Status of request, Login/Logout ,etc can be performed.It uses Database Management System (DBMS) such as MySQL also this is build on framework called Streamlit.This Application can be accessed over a LAN (Local Area Network)''/n This Application is developed by Shweta as a part of Training Project',
        unsafe_allow_html=True)

elif menu_id =='Employee':
    col1, col2, col3 = st.columns(3)
    with col1:
        pass
    with col3:
        pass
    with col2:
        if 'login' not in st.session_state:
            st.session_state['login'] = False
            st.session_state['uid'] = "s"
        if st.session_state['login'] == False:
            col3 = st.container()
            col3.markdown(
                """
                <style>
                .st-cv {
                    padding: 0px !important;
                    margin: 0px !important;
                }
                .st-cc {
                    padding: 0px !important;
                    margin: 0px !important;
                }
                </style>
                """,
                unsafe_allow_html=True
            )
            with col3:
                st.markdown(
                    '''<div style="text-align:center;"><img src="https://reddingrotary.org/wp-content/uploads/2019/01/Homepage-Icons-03.png" alt="image-description" width = "100"></div>''',
                    unsafe_allow_html=True)
                st.markdown('<div style="text-align:center;"><h1 style ="color:#b26e08;font-size:50px;">Employee Login</h1></div>', unsafe_allow_html=True)
                st.markdown(
                    '''<div style="text-align:center;"><p style="font-size:20px;">Please enter your credentials below</p></div>''',
                    unsafe_allow_html=True)

            with st.form("my_form"):
                buff, col, buff2 = st.columns([1, 3, 1])
                st.session_state['uid'] = col.text_input('Username')
                buff, col, buff2 = st.columns([1, 3, 1])
                pwd = col.text_input("Password", type='password')
                def add_bg_from_local(image_file):
                    with open(image_file, "rb") as image_file:
                        encoded_string = base64.b64encode(image_file.read())
                    st.markdown(
                        f"""
                          <style>
                          .stApp {{
                              background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
                              background-size: cover
                          }}
                          </style>
                          """,
                        unsafe_allow_html=True
                    )
                add_bg_from_local('C:/MyProject(ems)/ems/Scripts/images/emphome.png')

                submitted = col.form_submit_button("Submit")
                if submitted:
                    mydb = mysql.connector.connect(host="localhost", user="root", password="newrootpassword",
                                                   database="ems", auth_plugin='mysql_native_password')
                    c = mydb.cursor()
                    c.execute("select * from emp")
                    for row in c:
                        if (row[0] == st.session_state['uid'] and row[1] == pwd):
                            st.session_state['login'] = True
                            st.experimental_rerun()
                            break
                    if (st.session_state['login'] == False):
                        st.warning("Incorrect ID or Password")

    if st.session_state['login']:
        col1, col2, col3= st.columns([1,2,1])
        with col1:
            file_ = open("C:/MyProject(ems)/ems/Scripts/images/lft.png", "rb")
            contents = file_.read()
            style = """
                    <style>
                    .image-container {
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        margin: -40px;
                    }
                    .image-container img {
                        margin: 10px;
                        max-width: 100%;
                        max-height: 100%;
                        height: 350px;
                        width: 650px;
                    }
                    </style>
                """

            st.markdown(
                f'<div class="image-container">{style}'f'<img src="data:image/png;base64,{base64.b64encode(contents).decode("utf-8")}" /></div>',
                unsafe_allow_html=True,
            )
            with col2:
                file_ = open("C:/MyProject(ems)/ems/Scripts/images/mdle.png", "rb")
                contents = file_.read()
                style = """
                        <style>
                        .image-container {
                            display: flex;
                            justify-content: center;
                            align-items: center;
                            margin: -40px;
                        }
                        .image-container img {
                            margin: 10px;
                            max-width: 100%;
                            max-height: 100%;
                            height: 350px;
                            width: 650px;
                        }
                        </style>
                    """

                st.markdown(
                    f'<div class="image-container">{style}'f'<img src="data:image/png;base64,{base64.b64encode(contents).decode("utf-8")}" /></div>',
                    unsafe_allow_html=True,
                )
                with col3:
                    file_ = open("C:/MyProject(ems)/ems/Scripts/images/rht.png", "rb")
                    contents = file_.read()
                    style = """
                                    <style>
                                    .image-container {
                                        display: flex;
                                        justify-content: center;
                                        align-items: center;
                                        margin: -40px;
                                    }
                                    .image-container img {
                                        margin: 10px;
                                        max-width: 100%;
                                        max-height: 100%;
                                        height: 350px;
                                        width: 650px;
                                    }
                                    </style>
                                """

                    # Display the images inside a container with the CSS styles
                    st.markdown(
                        f'<div class="image-container">{style}'f'<img src="data:image/png;base64,{base64.b64encode(contents).decode("utf-8")}" /></div>',
                        unsafe_allow_html=True,
                    )


        type = option_menu(
            menu_title=None,
            options=["Personal Details", "Time Card Entry", "Leave Request", "Payroll Details", "Termination", "Logout"],
            icons=["file-person","calendar3", "", "receipt-cutoff", "person-workspace", "box-arrow-right"],
            menu_icon="cast",
            default_index=0,
            orientation="horizontal",
        )
        if type == "Personal Details":
            # Connect to MySQL database
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="newrootpassword",
                database="ems",
                auth_plugin='mysql_native_password'
            )
            mycursor = mydb.cursor()


            def upload_profile_pic():
                st.title("Employee Profile")

                profile_pic = st.file_uploader("Upload Profile Picture", type=["jpg", "jpeg", "png"])
                if profile_pic is not None:
                    user_id = st.session_state['uid']
                    temp_path = f"C:/MyProject(ems)/ems/Scripts/images/{user_id}.jpg"
                    with open(temp_path, "wb") as f:
                        f.write(profile_pic.read())
                    profile_image = temp_path
                    st.success("Profile picture uploaded successfully.")
                    st.image(profile_image, caption="Profile Picture")


                Name = st.text_input("Full Name")
                about = st.text_input("About Summary")
                designation = st.text_input("Designation")

                if st.button("Save"):
                    if Name and about and designation:

                        username = st.session_state['uid']
                        with open(profile_image, "rb") as f:
                            profile_img = f.read()
                        sql1 = "INSERT INTO employee (Username, profile_pic, name, about, designation) VALUES (%s, %s, %s, %s, %s)"
                        value = (username, profile_img, Name, about, designation)
                        mycursor.execute(sql1, value)
                        mydb.commit()
                        st.success("Profile information saved successfully!")
                    else:
                        st.warning("Please fill in all the details.")


            def view_profile():
                st.markdown("""
                    <style>
                    .highlight {
                        color: #b26e08;
                        text-align:left;
                        padding: 0px;
                        font-size: 45px;
                    }
                    </style>
                """, unsafe_allow_html=True)
                st.markdown('<h1 class="highlight">ABOUT ME', unsafe_allow_html=True)

                username = st.session_state['uid']
                mycursor.execute("SELECT * FROM employee WHERE Username=%s", (username,))
                result = mycursor.fetchone()
                if result:
                    try:
                        profile_image_data = result[1]
                        profile_image = Image.open(BytesIO(profile_image_data))
                        st.image(profile_image, width=170)

                        Name = st.write("Full Name:-", result[2])
                        designation = st.write("Designation:-", result[4])
                        about = st.write("Summary:-", result[3])

                        if st.button("Edit Details"):
                            designation = st.text_input("Designation", value=result[4])
                            about = st.text_area("About Summary", value=result[3])

                            if st.button("Save"):
                                if about and designation:
                                    # Update profile information in the database
                                    sql = "UPDATE employee SET about = %s, designation = %s WHERE Username = %s"
                                    values = (about, designation, username)
                                    mycursor.execute(sql, values)
                                    mydb.commit()
                                    st.success("Profile information updated successfully!")
                                else:
                                    st.warning("Please fill in all the details.")

                    except Exception as e:
                        st.error("Error: An unexpected error occurred while processing the image.")
                        st.error(str(e))
                else:
                    upload_profile_pic()
                    st.warning("No profile information found. Please update.")


            def main():
                if 'login' in st.session_state and st.session_state['login']:
                    view_profile()
                else:
                    upload_profile_pic()
            main()




        elif type == "Time Card Entry":
            st.markdown("""
                        <style>
                        .highlight {
                            color: #b26e08;
                            text-align:center;
                            padding: 0px;
                            font-size: 45px;
                        }
                        </style>
                        """, unsafe_allow_html=True)
            st.markdown('<h1 class="highlight">TIME CARD ENTRY', unsafe_allow_html=True)
            buff, col, buff2 = st.columns([1, 2, 1])
            selected_task = col.date_input('Select a date', datetime.today())
            start_time = col.time_input("Start Time")
            end_time = col.time_input("End Time")
            emp_id = st.session_state['uid']


            def check_if_time_card_entry_exists(emp_id, date):
                try:
                    conn = mysql.connector.connect(host="localhost", user="root", password="newrootpassword",
                                                   database="ems", auth_plugin='mysql_native_password')
                    cursor = conn.cursor()
                    cursor.execute("SELECT * FROM timecard WHERE Username=%s AND Date=%s", (emp_id, date))
                    entry = cursor.fetchone()
                    if entry is not None:
                        return True
                    else:
                        return False
                except:
                    st.error("Error fetching time card entries. Please try again later.")
                    return None


            def save_time_card_entry(selected_task, emp_id, start_time, end_time):
                try:
                    conn = mysql.connector.connect(host="localhost", user="root", password="newrootpassword",
                                                   database="ems", auth_plugin='mysql_native_password')
                    cursor = conn.cursor()
                    cursor.execute(
                        "INSERT INTO timecard (Date,Username, Start_time, End_time) VALUES (%s, %s, %s, %s)",
                        (selected_task, st.session_state['uid'], start_time, end_time))
                    conn.commit()
                    buff, col, buff2 = st.columns([1, 2, 1])
                    col.success("Time card entry submitted!")
                except:
                    buff, col, buff2 = st.columns([1, 2, 1])
                    st.error("Error saving time card entry. Please try again later.")


            submit = col.button("Submit")
            if submit:
                if check_if_time_card_entry_exists(emp_id, selected_task):
                    buff, col, buff2 = st.columns([1, 2, 1])
                    st.warning("You have already submitted a time card entry for this date.")
                elif start_time >= end_time:
                    buff, col, buff2 = st.columns([1, 2, 1])
                    st.warning("The start time must be earlier than the end time.")
                else:
                    save_time_card_entry(selected_task, st.session_state['uid'], start_time, end_time)

        elif type == "Leave Request":
            def submit_leave_request(emp_id, start_date, end_date, leave_type, reason):
                try:
                    conn = mysql.connector.connect(host="localhost", user="root", password="newrootpassword",
                                                   database="ems", auth_plugin='mysql_native_password')
                    cursor = conn.cursor()
                    cursor.execute(
                        "INSERT INTO leave_req (Username, start_date, end_date, leave_type, reason) VALUES (%s, %s, %s, %s, %s)",
                        (emp_id, start_date, end_date, leave_type, reason))
                    conn.commit()
                    st.success("Leave request submitted!")
                except:
                    st.error("Error saving leave request. Please try again later.")


            def validate_leave_request(emp_id, start_date, end_date):
                try:
                    conn = mysql.connector.connect(host="localhost", user="root", password="newrootpassword",
                                                   database="ems", auth_plugin='mysql_native_password')
                    cursor = conn.cursor()
                    cursor.execute(
                        "SELECT * FROM leave_req WHERE Username=%s AND status='Approved' AND ((start_date BETWEEN %s AND %s) OR (end_date BETWEEN %s AND %s))",
                        (emp_id, start_date, end_date, start_date, end_date))
                    overlapping_leave_requests = cursor.fetchall()
                    if len(overlapping_leave_requests) > 0:
                        st.warning("You have already been granted leave during this time period.")
                        return False
                    cursor.execute(
                        "SELECT * FROM timecard WHERE Username=%s AND Date BETWEEN %s AND %s",
                        (emp_id, start_date, end_date))
                    work_hours = cursor.fetchall()
                    if len(work_hours) > 0:
                        st.warning("You have already scheduled work during this time period.")
                        return False
                except:
                    st.error("Error validating leave request. Please try again later.")
                    return False


            st.markdown("""
                        <style>
                        .highlight {
                            color: #b26e08;
                            text-align:center;
                            padding: 0px;
                            font-size: 45px;
                        }
                        </style>
                        """, unsafe_allow_html=True)
            st.markdown('<h1 class="highlight">LEAVE REQUEST', unsafe_allow_html=True)
            col1, col2 = st.columns(2)
            emp_id = st.session_state['uid']
            with col1:
                def leave_request_form():
                    emp_id = st.session_state['uid']
                    buff, col, buff2 = st.columns([1, 2, 1])
                    start_date = col.date_input('Start date', datetime.today())
                    end_date = col.date_input('End date', datetime.today(), key=1)
                    leave_type = col.selectbox('Leave Type', ['Vacation', 'Sick', 'Personal'])
                    reason = col.text_input('Reason')
                    submit = col.button('Submit')
                    if submit:
                        submit_leave_request(emp_id, start_date, end_date, leave_type, reason)



                leave_request_form()
            with col2:
                def show_leave_chart(emp_id):

                    conn = mysql.connector.connect(host="localhost", user="root", password="newrootpassword",
                                                   database="ems", auth_plugin='mysql_native_password')
                    cursor = conn.cursor()
                    cursor.execute("SELECT leave_type, COUNT(*) FROM leave_req WHERE Username=%s GROUP BY Leave_type",
                                   (emp_id,))
                    result = cursor.fetchall()
                    df = pd.DataFrame(result, columns=["Leave Type", "Count"])
                    fig, ax = plt.subplots(figsize=(4, 4), facecolor='none', dpi=250)
                    ax.pie(df["Count"], labels=df["Leave Type"], autopct='%1.1f%%', startangle=95,
                           colors=["#FF4B4B", "#F6FF4B", "#4BFFAA"], textprops={'fontsize':20})
                    ax.axis('equal')
                    st.pyplot(fig)


                show_leave_chart(emp_id)


                def show_employee_leaves(emp_id):
                    try:
                        conn = mysql.connector.connect(host="localhost", user="root", password="newrootpassword",
                                                       database="ems", auth_plugin='mysql_native_password')
                        cursor = conn.cursor()
                        cursor.execute("SELECT * FROM leave_req WHERE Username=%s", (emp_id,))
                        leaves = cursor.fetchall()
                        if len(leaves) == 0:
                            st.warning("You have not applied for any leaves yet.")
                        else:
                            st.write("Your leaves:")
                            for leave in leaves:
                                st.write(f"- {leave[1]} to {leave[2]}, {leave[4]}")
                                st.write(f"  Status: {leave[5]}")
                    except:
                        st.error("Error fetching leaves. Please try again later.")


                buff, col, buff2 = st.columns([10, 5, 10])
                button = col.button("leave details")
                emp_id = st.session_state['uid']
                if button:
                    show_employee_leaves(emp_id)

        elif type == "Payroll Details":
            st.markdown("""
                        <style>
                        .highlight {
                            color: #b26e08;
                            text-align:center;
                            padding: 0px;
                            font-size: 45px;
                        }
                        </style>
                        """, unsafe_allow_html=True)
            st.markdown('<h1 class="highlight">SALARY DETAILS', unsafe_allow_html=True)

            def calculate_monthly_salary(employee_id, month, year):
                try:
                    conn = mysql.connector.connect(host="localhost", user="root", password="newrootpassword",database="ems", auth_plugin='mysql_native_password')
                    cursor = conn.cursor()

                    cursor.execute("SELECT day_rate FROM payroll WHERE Username = %s", (employee_id,))
                    day_rate = cursor.fetchone()[0]
                    day_rate = float(day_rate)

                    cursor.execute(
                        "SELECT SUM(TIME_TO_SEC(TIMEDIFF(End_time, Start_time))/3600) FROM timecard WHERE Username = %s AND MONTH(Date) = %s AND YEAR(Date) = %s",
                        (employee_id, month, year))
                    work_hours = cursor.fetchone()[0]
                    work_hours = float(work_hours)

                    cursor.execute(
                        "SELECT COUNT(*) FROM leave_req WHERE Username = %s AND MONTH(start_date) = %s AND YEAR(start_date) = %s AND status = 'approved'",
                        (employee_id, month, year))
                    leave_days = cursor.fetchone()[0]

                    gross_salary = day_rate * work_hours

                    deductions = gross_salary * 0.1

                    net_salary = gross_salary - deductions

                    st.write("Monthly Salary for Employee ID", employee_id, "for", month, "/", year)
                    st.write("Gross Salary: $", round(gross_salary))
                    st.write("Deductions: $", round(deductions))
                    st.write("Net Salary: $", round(net_salary))
                    # Generate a PDF version of the salary information
                    buffer = BytesIO()
                    c = canvas.Canvas(buffer)
                    c.drawString(100, 750, "Monthly Salary for Employee ID " + str(employee_id) + " for " + str(
                        month) + "/" + str(year))
                    # Draw the table header
                    c.drawString(100, 700, "Areas")
                    c.drawString(200, 700, "Amount")
                    # Draw the table rows
                    c.drawString(100, 675, "Gross Salary")
                    c.drawString(200, 675, "$" + str(round(gross_salary, 2)))
                    c.drawString(100, 650, "Deductions")
                    c.drawString(200, 650, "$" + str(round(deductions, 2)))
                    c.drawString(100, 625, "Net Salary")
                    c.drawString(200, 625, "$" + str(round(net_salary, 2)))
                    c.save()
                    pdf_bytes = buffer.getvalue()
                    st.download_button("Download PDF", data=pdf_bytes, file_name="salary.pdf", mime="application/pdf")


                    x_labels = ['Gross Salary', 'Deductions', 'Net Salary']
                    y_values = [gross_salary, deductions, net_salary]
                    fig, ax = plt.subplots(figsize=(6,2.5))
                    ax.bar(x_labels, y_values, color=['lightgreen', 'pink', 'skyblue'])
                    ax.set_title("Monthly Salary for Employee ID " + str(employee_id) + " for " + str(month) + "/" +str(year), fontsize=11)
                    ax.set_ylabel("Salary ($)", fontsize=8)
                    ax.tick_params(axis='x', labelsize=5)
                    ax.tick_params(axis='y', labelsize=5)
                    for i, v in enumerate(y_values):
                        ax.text(i, v , str(round(v)), color='black', ha='center', fontsize ='5', fontweight='bold')
                    plt.tight_layout()
                    st.pyplot(fig)

                except:
                    st.error("No pay rate found or No attendance captured for this month. Please contact your employer")

            employee_id = st.session_state['uid']
            buff, col, buff2 = st.columns([1, 2, 1])
            month = col.text_input("Enter Month (MM/00)")
            year = col.text_input("Enter Year (YYYY/2000)")

            if col.button("Calculate Monthly Salary"):
                employee_id = st.session_state['uid']
                mydb = mysql.connector.connect(host="localhost", user="root", password="newrootpassword",
                                               database="ems", auth_plugin='mysql_native_password')
                mycursor = mydb.cursor()
                mycursor.execute("SELECT * FROM payroll")
                data = mycursor.fetchall()  # Fetch results after executing query
                existing_data = [row[0] for row in data]  # Extract employee_ids from fetched data

                # Check if employee_id is already present in the payroll table
                if employee_id not in existing_data:
                    sql = "INSERT INTO payroll (Username) VALUES (%s)"
                    values = (employee_id,)
                    mycursor.execute(sql, values)
                    mydb.commit()

                calculate_monthly_salary(employee_id, month, year)

        elif type == "Termination":
            def update_term(username, termination_date, termination_reason, relieving_date):
                mydb = mysql.connector.connect(host="localhost", user="root", password="newrootpassword",
                                               database="ems", auth_plugin='mysql_native_password')
                mycursor = mydb.cursor()
                sql = "INSERT INTO termination (Username, termination_date, termination_reason, reliving_date) VALUES (%s, %s, %s, %s)"
                values = (username, termination_date, termination_reason, relieving_date)
                mycursor.execute(sql, values)
                mydb.commit()


            def terminate_employee():
                st.markdown("""
                            <style>
                            .highlight {
                                color: #b26e08;
                                text-align:center;
                                padding: 0px;
                                font-size: 45px;
                            }
                            </style>
                            """, unsafe_allow_html=True)
                st.markdown('<h1 class="highlight">Employee Termination', unsafe_allow_html=True)
                buff, col, buff2 = st.columns([1, 2, 1])
                username = st.session_state['uid']
                termination_date = col.date_input("Termination Date", key="termination_date")
                termination_reason = col.text_input("Termination Reason")

                relieving_date = None
                if termination_date:
                    relieving_date = termination_date + timedelta(days=60)  # Add 60 days to the termination date
                    col.info("Relieving Date: {}".format(relieving_date))

                if col.button("Submit"):
                    if termination_date and termination_reason:
                        if relieving_date:
                            update_term(username, termination_date, termination_reason, relieving_date)
                            col.success("Termination details updated successfully!")
                        else:
                            col.warning("Failed to calculate relieving date.")
                    else:
                        col.warning("Please fill in all the details.")
                if col.button("Show Termination status"):
                    try:
                        username = st.session_state['uid']
                        mydb = mysql.connector.connect(host="localhost", user="root", password="newrootpassword",
                                                       database="ems", auth_plugin='mysql_native_password')
                        mycursor = mydb.cursor()
                        sql = f"Select employment_status from termination where Username='{username}'"
                        value = (username)
                        mycursor.execute(sql, value)
                        mydb.commit()
                    except:
                        col.error("No Termination request found.")


            terminate_employee()


        elif type == "Logout":
            st.markdown(
                '''<div style="text-align:center;"><img src="https://www.svgrepo.com/download/28236/exit.svg" alt="image-description" width = "300"></div>''',
                unsafe_allow_html=True)
            st.markdown("""
                                    <style>
                                    .highlight {
                                        color: #b26e08;
                                        text-align:center;
                                        padding: 0px;
                                        font-size: 40px;
                                    }
                                    </style>
                                    """, unsafe_allow_html=True)
            st.markdown("<h1 class='highlight'>Oh No! you're leaving...<br> Are you sure?</br> ", unsafe_allow_html=True)
            m = st.markdown("""
                          <style>
                          div.stButton > button:first-child {
                              text-align: center;
                              border-radius: 11px 11px 11px 11px;
                              height: 3em;
                              width: 11em;
                              margin: 0 auto;
                              display: block;
                          }
                          </style>""", unsafe_allow_html=True)

            if st.button("Yes, Please let me out", key="my_button"):
                st.session_state['login'] = False


elif menu_id == 'Employer':
    col1, col2, col3 = st.columns(3)
    with col1:
        pass
    with col3:
        pass
    with col2:
        if 'elogin' not in st.session_state:
            st.session_state['elogin'] = False
            st.session_state['eid'] = "s"
        if st.session_state['elogin'] == False:

            col3 = st.container()

            col3.markdown(
                """
                <style>
                .st-cv {
                    padding: 0px !important;
                    margin: 0px !important;
                }
                .st-cc {
                    padding: 0px !important;
                    margin: 0px !important;
                }
                </style>
                """,
                unsafe_allow_html=True
            )

            with col3:
                st.markdown(
                    '''<div style="text-align:center;"><img src="https://reddingrotary.org/wp-content/uploads/2019/01/Homepage-Icons-03.png" alt="image-description" width = "100"></div>''',
                    unsafe_allow_html=True)
                st.markdown(
                    '<div style="text-align:center;"><h1 style ="color:#b26e08;font-size:50px;">Employer Login</h1></div>',
                    unsafe_allow_html=True)
                st.markdown(
                    '''<div style="text-align:center;"><p style="font-size:20px;">Please enter your credentials below</p></div>''',
                    unsafe_allow_html=True)
            with st.form("my_form"):
                buff, col, buff2 = st.columns([1, 3, 1])
                st.session_state['eid'] = col.text_input('Username')
                pwd = col.text_input("Password", type='password')
                def add_bg_from_local(image_file):
                    with open(image_file, "rb") as image_file:
                        encoded_string = base64.b64encode(image_file.read())
                    st.markdown(
                        f"""
                       <style>
                       .stApp {{
                           background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
                           background-size: cover
                       }}
                       </style>
                       """,
                        unsafe_allow_html=True
                    )
                add_bg_from_local('C:/MyProject(ems)/ems/Scripts/images/emphome.png')
                submitted = col.form_submit_button("Submit")
                if submitted:
                    mydb = mysql.connector.connect(host="localhost", user="root", password="newrootpassword",
                                                   database="ems", auth_plugin='mysql_native_password')
                    c = mydb.cursor()
                    c.execute("select * from emr")
                    for row in c:
                        if (row[0] == st.session_state['eid'] and row[1] == pwd):
                            st.session_state['elogin'] = True
                            st.experimental_rerun()
                            break
                    if (st.session_state['elogin'] == False):
                        st.warning("Incorrect ID or Password")
    if st.session_state['elogin']:
        with st.container():
            st.markdown(
                "<div style='text-align:center'><img src='https://webstockreview.net/images/clipart-computer-business-woman-1.png', width='300' height='225' ;></img></div>",
                unsafe_allow_html=True)
            st.markdown("")

            with st.expander("Click here to view employee data"):

                mydb = mysql.connector.connect(host="localhost", user="root", password="newrootpassword",
                                               database="ems", auth_plugin='mysql_native_password')


                mycursor = mydb.cursor()
                mycursor.execute("SELECT * FROM employee")
                data = mycursor.fetchall()


                df = pd.DataFrame(data, columns=["Username","profile_pic", "Name", "About", "Designation"])

                selected_columns = ["Username", "Name", "Designation"]
                buff, col, buff2 = st.columns([1, 3, 1])
                col.subheader("Employees Details")
                col.dataframe(df[selected_columns])


        mydb = mysql.connector.connect(host="localhost", user="root", password="newrootpassword",
                                       database="ems", auth_plugin='mysql_native_password')
        mycursor = mydb.cursor()


        def update_payroll_data(username, day_rate, month, year, status):
            check_query = "SELECT * FROM payroll WHERE username = %s AND month = %s"
            check_values = (username, month)
            mycursor.execute(check_query, check_values)
            existing_row = mycursor.fetchone()

            if existing_row:
                update_query = "UPDATE payroll SET day_rate = %s, year = %s, status = %s WHERE username = %s AND month = %s"
                update_values = (day_rate, year, status, username, month)
                mycursor.execute(update_query, update_values)
            else:
                insert_query = "INSERT INTO payroll (username, day_rate, month, year, status) VALUES (%s, %s, %s, %s, %s)"
                insert_values = (username, day_rate, month, year, status)
                mycursor.execute(insert_query, insert_values)

            mydb.commit()


        with st.container():
            st.markdown(
                "<div style='text-align:center'><img src='https://1.bp.blogspot.com/-FvZ54v4EyeY/XoNz3afFIQI/AAAAAAAAPUQ/GqDI206F3lMROLpYBxnoH88-_15PWXMBACLcBGAsYHQ/s640/common%2Bpayroll%2Bprocessing%2Bmistakes.png', width='300' height='225';></img></div>",
                unsafe_allow_html=True)
            st.markdown("")

            with st.expander("Click here to view and update employee payroll data"):
                mycursor.execute("SELECT * FROM payroll")
                data = mycursor.fetchall()

                df = pd.DataFrame(data, columns=["Username", "Day Rate", "Month", "Year", "Status"])
                buff, col, buff2 = st.columns([1, 3, 1])
                col.write(df)

                buff, col, buff2 = st.columns([1, 3, 1])
                col.subheader("Update Payroll Details")
                selected_username = col.selectbox("Select Username", options=df['Username'].unique())
                selected_data = df[df['Username'] == selected_username].iloc[0]

                if selected_data['Month'] is not None:
                    month_value = datetime.strptime(selected_data['Month'], '%Y-%m-%d').date()
                else:
                    month_value = datetime.now().date()

                if selected_data['Day Rate'] is not None:
                    day_rate = col.number_input(f"Day Rate - {selected_data['Day Rate']}",
                                                value=float(selected_data['Day Rate']))
                else:
                    day_rate = col.number_input("Day Rate", value=0.0)

                month = col.date_input(f"Month - {selected_data['Month']}", value=month_value)
                year = col.text_input(f"Year - {selected_data['Year']}", value=str(selected_data['Year']))
                status = col.selectbox(f"Status - {selected_data['Status']}", options=["Delivered", "Pending"], index=0)

                if col.button("Update"):
                    month_value_str = month.strftime('%Y-%m-%d')
                    update_payroll_data(selected_username, day_rate, month_value_str, year, status)
                    col.success("Payroll data updated successfully!")
                    st.experimental_rerun()

                    selected_data['Day Rate'] = day_rate
                    selected_data['Month'] = month.strftime('%Y-%m-%d')
                    selected_data['Year'] = int(year)
                    selected_data['Status'] = status

                df[df['Username'] == selected_username] = selected_data

        with st.container():
            st.markdown(
                "<div style='text-align:center'><img src='https://www.udteschool.com/img/work/Leave.png', width='300' height='230' ;></img></div>",
                unsafe_allow_html=True)
            st.markdown("")
            with st.expander("Click here to view and update employee Leave Requests"):

                mydb = mysql.connector.connect(host="localhost", user="root", password="newrootpassword",
                                               database="ems", auth_plugin='mysql_native_password')
                c = mydb.cursor()
                c.execute("SELECT * FROM leave_req")
                data = c.fetchall()

                df = pd.DataFrame(
                    data,
                    columns=['Username', 'start_date', 'end_date', 'leave_type', 'reason', 'status']
                )
                buff, col, buff2 = st.columns([1, 3, 1])
                col.dataframe(df)
                def update_status(new_status, username, start_date):
                    mydb = mysql.connector.connect(host="localhost", user="root", password="newrootpassword",
                                                   database="ems", auth_plugin='mysql_native_password')
                    c = mydb.cursor()
                    c.execute('UPDATE leave_req SET status = %s WHERE Username = %s AND start_date = %s',
                              (new_status, username, start_date))
                    mydb.commit()

                c = mydb.cursor()
                c.execute("SELECT DISTINCT Username FROM leave_req")
                usernames = [row[0] for row in c.fetchall()]
                buff, col, buff2 = st.columns([1, 3, 1])
                col.subheader("Update Leave Status")
                username = col.selectbox("Select Employee:", usernames)

                c.execute("SELECT start_date FROM leave_req WHERE Username = %s", (username,))
                start_dates = [row[0] for row in c.fetchall()]

                start_date = col.selectbox("Select start date:", start_dates)

                new_status = col.selectbox("Select Status:", ['Pending', 'Approved', 'Declined'])

                if col.button("Update", key=2):
                    if username and new_status and start_date:
                        update_status(new_status, username, start_date)
                        st.experimental_rerun()
                        col.success("Leave status updated successfully!")
                    else:
                        col.error("Please enter valid Employee ID and select Status.")

        with st.container():
            st.markdown(
                "<div style='text-align:center'><img src='https://media.istockphoto.com/vectors/businesswoman-leaving-job-vector-vector-id532398604?k=6&m=532398604&s=612x612&w=0&h=k0LUIvyp746lMNaxynobJDZuElNIObplDWlJLY8Ngv4=', width='300' height='225' ;></img></div>",
                unsafe_allow_html=True)
            st.markdown("")
        def get_data_from_database():
            try:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="newrootpassword",
                    database="ems",
                    auth_plugin='mysql_native_password'
                )
            except mysql.connector.Error as err:
                st.error(f"Error connecting to MySQL database: {err}")

            # Retrieve the employee data from the database
            try:
                mycursor = mydb.cursor()
                mycursor.execute("SELECT * FROM Termination")
                data = mycursor.fetchall()
            except mysql.connector.Error as err:
                st.error(f"Error retrieving employee data: {err}")


            df = pd.DataFrame(
                data,
                columns=["Username", "Name", "Salary", "Relieving Date", "Employment status"]
            )

            return df
        def update_employee_status(employee_id, new_status):
            try:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="newrootpassword",
                    database="ems",
                    auth_plugin='mysql_native_password'
                )
            except mysql.connector.Error as err:
                st.error(f"Error connecting to MySQL database: {err}")

            mycursor = mydb.cursor()
            mycursor.execute("UPDATE Termination SET employment_status = %s WHERE Username = %s",
                             (new_status, employee_id))
            mydb.commit()

        df = get_data_from_database()

        with st.expander("Click here to view and update Employee Termination details"):
            buff, col, buff2 = st.columns([1, 3, 1])
            col.write(df)

            # Update employment status
            buff, col, buff2 = st.columns([1, 3, 1])
            col.subheader("Update Employment Status")
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="newrootpassword",
                database="ems",
                auth_plugin='mysql_native_password'
            )
            mycursor = mydb.cursor()
            mycursor.execute("SELECT Username FROM Termination")
            data = mycursor.fetchall()
            options = []
            for row in data:
                option = row[0]
                options.append(option)
            buff, col, buff2 = st.columns([1, 3, 1])
            employee_id = col.selectbox("Enter Employee ID:", options)
            new_status = col.selectbox("Select New Employment Status:", ['Approved', 'Declined'])
            if col.button("Update", key=666):
                if employee_id and new_status:
                    update_employee_status(employee_id, new_status)
                    col.success("Employment status updated successfully!")
                    st.experimental_rerun()
                else:
                    col.error("Please enter valid Employee ID and select a new Employment Status.")

        buff, col, buff2 = st.columns([10, 3, 10])
        Btn = col.button("LOGOUT")
        if Btn:
            st.session_state['elogin'] = False

elif menu_id == "Feedback":
    def add_bg_from_local(image_file):
        with open(image_file, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        st.markdown(
            f"""
           <style>
           .stApp {{
               background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
               background-size: cover
           }}
           </style>
           """,
            unsafe_allow_html=True
        )


    add_bg_from_local('C:/MyProject(ems)/ems/Scripts/images/emphome.png')
    def feedback_form():
        st.markdown("""
                    <style>
                    .highlight {
                        color: #b26e08;
                        text-align:center;
                        padding: 5px;
                        font-size: 45px;
                    }
                    </style>
                    """, unsafe_allow_html=True)
        st.markdown('<h1 class="highlight">Feedback Form', unsafe_allow_html=True)

        def update_feedback(name, Username, feedback):
            mydb = mysql.connector.connect(host="localhost", user="root", password="newrootpassword",
                                           database="ems", auth_plugin='mysql_native_password')
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM feedback WHERE Username = %s", (Username,))
            existing_record = mycursor.fetchone()

            if existing_record:

                sql = "UPDATE feedback SET Name = %s, Feedback = %s WHERE Username = %s"
                values = (name, feedback, Username)
                mycursor.execute(sql, values)
                mydb.commit()
            else:

                sql = "INSERT INTO feedback (Name, Username, Feedback) VALUES (%s, %s, %s)"
                values = (name, Username, feedback)
                mycursor.execute(sql, values)
                mydb.commit()


        buff, col, buff2 = st.columns([1, 3, 1])
        name = col.text_input("Name")
        Username = col.text_input("Username")
        feedback = col.text_area("Feedback", height=150)


        if col.button("Submit"):

            if name and Username and feedback:
                update_feedback(name, Username, feedback)
                col.success("Thank you for your feedback!")
            else:
                col.warning("Please fill in all the fields.")

    feedback_form()





















































