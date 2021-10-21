from flask import Blueprint, render_template, request, flash
from webserver import db 


views = Blueprint("views", __name__)

@views.route("/", methods=["POST", "GET"])
@views.route("/home", methods=["POST", "GET"])
def main():
	if request.method =="POST":
		first_name = request.form["first_name"]
		last_name =  request.form["last_name"]
		phone_number = request.form["phone_number"]
		email =  request.form["email"]
		linked_in = request.form["linked_in"]
		twitter = request.form["twitter"]
		college_name = request.form["college_name"]
		college_degree = request.form["college_degree"]
		field_of_study = request.form["field_of_study"]
		highschool_name = request.form["highschool_name"]
		highschool_degree = request.form["highschool_degree"]
		highschool_stream = request.form["highschool_stream"]
		school_name = request.form["school_name"]
		school_degree = request.form["school_degree"]
		job_title = request.form["job_title"]
		employer = request.form["employer"]
		w_description = request.form["w_description"]
		work_city = request.form["work_city"]
		work_state = request.form["work_state"]
		start_date = request.form["start_date"]
		end_date = request.form["end_date"]
		project1_title = request.form["project1_title"]
		project1_description = request.form["project1_description"]
		project2_title = request.form["project2_title"]
		project2_description = request.form["project2_description"]
		project3_title = request.form["project3_title"]
		project3_description = request.form["project3_description"]

		mycursor = db.cursor()

		list = (first_name, last_name, phone_number, email,
		linked_in, twitter, college_name, college_degree, field_of_study, highschool_name, highschool_degree, highschool_stream, school_name, school_degree,
		job_title, employer, w_description, work_city, work_state,start_date, end_date, project1_title, project1_description, project2_title, project2_description, project3_title, project3_description)

		sql = '''INSERT INTO resume_table(first_name, last_name, phone_number, email,
		linked_in, twitter, college_name, college_degree, field_of_study, highschool_name, highschool_degree, highschool_stream, school_name, school_degree,
		job_title, employer, w_description, work_city, work_state, start_date, end_date, project1_title, project1_description, project2_title, project2_description, project3_title, project3_description)
		VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
		
		mycursor.execute(sql, list)
		db.commit()
		id = mycursor.lastrowid
		flash('Data Submited Successfully')
		print(id)
		return render_template('index.html', id=id)
	else:
		return render_template('index.html')


@views.route("/preview/<int:id>", methods=['GET', 'POST'])
def preview(id):
	mycursor = db.cursor()
	mycursor.execute('''SELECT * FROM resume_table WHERE id = %s''', (id, ))
	result = list(mycursor.fetchone())
	mlist = ('id','first_name', 'last_name', 'phone_number', 'email',
		'linked_in', 'twitter', 'college_name', 'college_degree', 'field_of_study', 'highschool_name', 'highschool_degree', 'highschool_stream', 'school_name', 'school_degree',
		'job_title', 'employer', 'w_description', 'work_city', 'work_state', 'start_date', 'end_date', 'project1_title', 'project1_description', 'project2_title', 'project2_description', 'project3_title', 'project3_description', 'datetime')
	Dict = dict(zip(mlist,result))
	print(Dict)
	return render_template("profile.html", Dict=Dict)