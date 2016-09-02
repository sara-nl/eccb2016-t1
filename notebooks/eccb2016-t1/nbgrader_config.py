c = get_config()

###############################################################################
# Begin additions by nbgrader quickstart
###############################################################################

# You only need this if you are running nbgrader on a shared
# server set up.
c.NbGrader.course_id = "eccb2016-t1"

# Update this list with other assignments you want
c.NbGrader.db_assignments = [dict(name="Set 1 - Tutorial"), dict(name="Set 2 - Extra")]

c.NbGrader.db_students = [
    dict(id="bitdiddle", first_name="Ben", last_name="Bitdiddle"),
    dict(id="hacker", first_name="Alyssa", last_name="Hacker"),
    dict(id="reasoner", first_name="Louis", last_name="Reasoner")
]

c.ClearSolutions.code_stub = '# PLEASE FILL IN YOUR CODE HERE'
