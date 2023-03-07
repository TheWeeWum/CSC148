import pytest

# You may need to import pytest in order to run your tests.
# You are free to import hypothesis and use hypothesis for testing.
# This file will not be graded for style with PythonTA
# import pytest
# import hypothesis
from course import *
from survey import *
from criterion import *
from grouper import *
import random

list_of_students1 = [
    Student(5, 'Liam'),
    Student(2, 'Ian'),
    Student(4, 'John'),
    Student(3, 'Raon'),
    Student(1, 'Tina'),
    Student(0, "Zi Qi")
]
list_of_students2 = [
    Student(6, 'Kevin'),
    Student(7, 'Charlie'),
    Student(8, 'Mark'),
    Student(9, 'Laura'),
    Student(10, 'Gina'),
    Student(11, 'Alain')
]
list_of_students_duplicates = [
    Student(6, 'Dorothee'),
    Student(7, 'Kabir'),
    Student(8, 'Selin'),
    Student(9, "Brooke"),
    Student(1, 'Tina'),
    Student(0, "Zi Qi")
]
list_of_students_same_id = [
    Student(0, 'Tony')
]

group_one = Group([Student(100, 'Single')])
group_norm = Group(list_of_students1)
group_norm2 = Group(list_of_students2)
group_duplicates = Group(list_of_students_duplicates)

list_of_questions1 = [
    YesNoQuestion(0, "Do you have a pet"),
    YesNoQuestion(1, "Are you over 30"),
    YesNoQuestion(2, "Do you own a car"),
    MultipleChoiceQuestion(3, "Cat or Dog", ['Cat', "Dog"]),
    MultipleChoiceQuestion(4, "Birth month",
                           ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']),
    NumericQuestion(5, "Age", 10, 100),
    NumericQuestion(6, "Monthly income", 0, 20000),
    CheckboxQuestion(7, "What pets do you own", ['Cat', 'Dog', 'Fish', 'Hamster', 'Bird', 'Gecko']),
    CheckboxQuestion(8, "Which streamers do you watch if any",
                     ['Ludwig', 'Valkyrae', 'Hassan Abi', 'Sykkuno', 'QT Cinderella'])
]
list_of_questions2 = [
    YesNoQuestion(9, "Do you have a Car"),
    MultipleChoiceQuestion(10, "Car or Truck", ['Car', 'Truck']),
    NumericQuestion(11, "How many siblings do you have", 0, 14),
    CheckboxQuestion(12, "What do you put on your sandwich",
                     ['Lettuce', 'Tomato', 'Ham', 'Pickles', 'Bacon', 'Mayo', 'Mustard', 'Ketchup'])
]
list_of_questions_same_questions_diff_id = [
    YesNoQuestion(13, "Do you have a pet"),
    YesNoQuestion(14, "Are you over 30"),
    YesNoQuestion(15, "Do you own a car"),
    MultipleChoiceQuestion(16, "Cat or Dog", ['Cat', "Dog"]),
    MultipleChoiceQuestion(17, "Birth month",
                           ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']),
    NumericQuestion(18, "Age", 10, 100),
    NumericQuestion(19, "Monthly income", 0, 20000),
    CheckboxQuestion(20, "What pets do you own", ['Cat', 'Dog', 'Fish', 'Hamster', 'Bird', 'Gecko']),
    CheckboxQuestion(21, "Which streamers do you watch if any",
                     ['Ludwig', 'Valkyrae', 'Hassan Abi', 'Sykkuno', 'QT Cinderella']),
    YesNoQuestion(22, "Do you have a Car"),
    MultipleChoiceQuestion(23, "Car or Truck", ['Car', 'Truck']),
    NumericQuestion(24, "How many siblings do you have", 0, 14),
    CheckboxQuestion(25, "What do you put on your sandwich",
                     ['Lettuce', 'Tomato', 'Ham', 'Pickles', 'Bacon', 'Mayo', 'Mustard', 'Ketchup'])
]
list_of_questions_used_ids_new_types = [
    YesNoQuestion(0, "Do you like snow"),
    NumericQuestion(1, "Number of pets", 0, 20),
    MultipleChoiceQuestion(2, "Fruits", ['Apple', 'Orange', 'Peach'])
]
list_of_questions_empty = []
list_of_questions_one_question = [YesNoQuestion(100, "Sleepy?")]

mc_question = MultipleChoiceQuestion(0, "MC question", [
    'a', 'b', 'c', 'd', 'Dog', 'Cat', 'Fish', 'Bird', 'Hamster'])
valid_mc_answers = [
    Answer('a'),
    Answer('b'),
    Answer('c'),
    Answer('d'),
    Answer('Dog'),
    Answer('Cat'),
    Answer('Fish'),
    Answer('Bird'),
    Answer('Hamster')
]
invalid_mc_answers = [
    Answer(True),
    Answer(False),
    Answer('Horse'),
    Answer(['Twelve']),
    Answer([]),
    Answer(10),
    Answer(0),
    Answer(['a', 'b'])
]

num_question = NumericQuestion(1, "Num question", 10, 100)
valid_num_answers = [Answer(x) for x in range(10, 101)]

invalid_num_answers = [
    Answer(True),
    Answer(False),
    Answer('Horse'),
    Answer(['Twelve']),
    Answer([]),
    Answer(9),
    Answer(101),
    Answer(['a', 'b']),
    Answer('a'),
    Answer('Dog')
]

yn_question = YesNoQuestion(2, "YN question")
valid_yn_answers = [Answer(True), Answer(False)]
invalid_yn_answers = [
    Answer('Horse'),
    Answer(['Twelve']),
    Answer([]),
    Answer(9),
    Answer(101),
    Answer(['a', 'b']),
    Answer('a'),
    Answer('Dog'),
    Answer(10),
    Answer(100),
    Answer(50)
]

cb_question = CheckboxQuestion(3, "CB question", [
    'a', 'b', 'c', 'd', 'Dog', 'Cat', 'Fish', 'Bird', 'Hamster'])
valid_cb_answers = [
    Answer(['a']),
    Answer(['b']),
    Answer(['c']),
    Answer(['d']),
    Answer(['Dog']),
    Answer(['Cat']),
    Answer(['Fish']),
    Answer(['Bird']),
    Answer(['Hamster']),
    Answer(['a', 'b']),
    Answer(['a', 'b', 'c', 'd', 'Dog', 'Cat', 'Fish', 'Bird', 'Hamster']),
    Answer(['a', 'Hamster', 'b'])
]
invalid_cb_answers = [
    Answer(True),
    Answer(False),
    Answer('Horse'),
    Answer(['Twelve']),
    Answer([]),
    Answer(10),
    Answer(0),
    Answer(['Dog', 'Dog', 'Cat', 'a'])
]

main_survey_one_question = Survey(list_of_questions_one_question)
main_survey_short = Survey(list_of_questions1[0:2])

if True:
    q1 = NumericQuestion(0, "Year", 1, 6)
    q2 = MultipleChoiceQuestion(1, "College", ['Victoria', 'New', 'Woodsworth', 'Victoria', 'Trinity'])
    priya = Student(0, 'Priya')
    priya.set_answer(q1, Answer(3))
    priya.set_answer(q2, Answer('Victoria'))
    alain = Student(1, 'Alain')
    alain.set_answer(q1, Answer(2))
    alain.set_answer(q2, Answer('New'))
    zoe = Student(2, 'Zoe')
    zoe.set_answer(q1, Answer(3))
    zoe.set_answer(q2, Answer('Woodsworth'))
    francis = Student(3, 'Francis')
    francis.set_answer(q1, Answer(3))
    francis.set_answer(q2, Answer('Victoria'))
    mohammed = Student(4, 'Mohammed')
    mohammed.set_answer(q1, Answer(4))
    mohammed.set_answer(q2, Answer('Woodsworth'))
    xiaoyuan = Student(5, 'Xiaoyuan')
    xiaoyuan.set_answer(q1, Answer(5))
    xiaoyuan.set_answer(q2, Answer('New'))
    rohit = Student(6, 'Rohit')
    rohit.set_answer(q1, Answer(2))
    rohit.set_answer(q2, Answer('New'))
    yimin = Student(7, 'Yimin')
    yimin.set_answer(q1, Answer(3))
    yimin.set_answer(q2, Answer('Trinity'))

    grace = Student(8, 'Grace')
    grace.set_answer(q1, Answer(5))
    grace.set_answer(q2, Answer('Woodsworth'))
    clair = Student(9, 'Clair')
    clair.set_answer(q1, Answer(1))
    clair.set_answer(q2, Answer('Woodsworth'))
    kai = Student(10, 'Kai')
    kai.set_answer(q1, Answer(1))
    kai.set_answer(q2, Answer('Woodsworth'))

    liam = Student(5, 'Liam')
    ian = Student(2, 'Ian')
    john = Student(4, 'John')
    raon = Student(3, 'Raon')
    tina = Student(1, 'Tina')
    ziqi = Student(0, "Zi Qi")

    liam.set_answer(list_of_questions1[0], Answer(True))
    liam.set_answer(list_of_questions1[1], Answer(True))
    ian.set_answer(list_of_questions1[0], Answer(False))
    ian.set_answer(list_of_questions1[1], Answer(False))
    john.set_answer(list_of_questions1[0], Answer(False))
    john.set_answer(list_of_questions1[1], Answer(True))
    raon.set_answer(list_of_questions1[0], Answer(True))
    raon.set_answer(list_of_questions1[1], Answer(False))
    tina.set_answer(list_of_questions1[0], Answer(True))
    tina.set_answer(list_of_questions1[1], Answer(True))
    ziqi.set_answer(list_of_questions1[0], Answer(False))
    ziqi.set_answer(list_of_questions1[1], Answer(True))

given_stu1 = [priya, alain, zoe, francis]
given_stu2 = [mohammed, xiaoyuan, rohit, ]
given_stu3 = [grace, clair, kai]
given_questions = [
    q1,
    q2
]

list_of_students1_with_answers = [
    liam,
    ian,
    john,
    raon,
    tina,
    ziqi
]


def empty_course() -> Course:
    return Course('Test')


def course_with_students(num_students: int) -> Course:
    """
    Note all students will have the same name
    And IDS ranging from 0 to num_students - 1
    """
    course = Course('Test')
    for i in range(num_students):
        course.enroll_students([Student(i, f"Student{i}")])
    return course


def course_with_students_with_answers(num_students: int, questions: list[
    Question | NumericQuestion | YesNoQuestion | MultipleChoiceQuestion | CheckboxQuestion]) -> Course:
    course = course_with_students(num_students)
    for q in questions:
        for stu in course.get_students():
            if isinstance(q, NumericQuestion):
                ans = random.randint(q._min, q._max)
                stu.set_answer(q, Answer(ans))

            elif isinstance(q, YesNoQuestion):
                ans = random.randint(0, 1)
                stu.set_answer(q, Answer(bool(ans)))

            elif isinstance(q, CheckboxQuestion):
                # stu.set_answer(q, Answer(random.choice(q._options)))
                num_elements = random.randint(1, len(q._options) - 1)
                stu.set_answer(q, Answer(random.sample(q._options, k=num_elements)))

            elif isinstance(q, MultipleChoiceQuestion):
                stu.set_answer(q, Answer(random.choice(q._options)))

            else:
                raise ZeroDivisionError

    return course


def course_with_students_with_set_answers(questions: list[Question | NumericQuestion | YesNoQuestion | MultipleChoiceQuestion | CheckboxQuestion]) -> Course:
    course = course_with_students(5)
    for q in questions:
        for i, stu in enumerate(course.get_students()):
            if isinstance(q, NumericQuestion):
                ans = int(i * q._max - q._min)
                stu.set_answer(q, Answer(ans))

            elif isinstance(q, YesNoQuestion):
                ans = bool(i % 2)
                stu.set_answer(q, Answer(bool(ans)))

            elif isinstance(q, CheckboxQuestion):
                stu.set_answer(q, Answer(q._options[i]))

            elif isinstance(q, MultipleChoiceQuestion):
                stu.set_answer(q, Answer(q._options[0:i]))

            else:
                raise ZeroDivisionError

    return course


def generic_questions():
    questions = [YesNoQuestion(0, "YN Question"),
                 NumericQuestion(1, "Num Question", 0, 10),
                 MultipleChoiceQuestion(2, "MC Question", ['a', 'b', 'c', 'd', 'e', 'f']),
                 CheckboxQuestion(3, "CB Question", ['a', 'b', 'c', 'd', 'e', 'f'])
                 ]
    return questions


###############################################################################
# Task 2 Test cases Student class
###############################################################################
class TestStudent:
    def test_general_has_answer(self) -> None:
        stu = Student(0, "Liam")
        question = NumericQuestion(0, "How old are you", 16, 100)
        question1 = NumericQuestion(1, "How old are you", 16, 100)
        question2 = NumericQuestion(2, "How old are you", 16, 100)
        question3 = NumericQuestion(3, "How old are you", 16, 100)

        ans = Answer(18)
        stu.set_answer(question, ans)
        assert stu.has_answer(question) is True

        ans_too_young = Answer(10)
        stu.set_answer(question1, ans_too_young)
        assert stu.has_answer(question1) is False

        ans_too_old = Answer(200)
        stu.set_answer(question2, ans_too_old)
        assert stu.has_answer(question2) is False

        ans_not_int = Answer("twenty")
        stu.set_answer(question3, ans_not_int)
        assert stu.has_answer(question3) is False

        unanswered_question = NumericQuestion(10, "No answer!", 1, 2)
        assert stu.has_answer(unanswered_question) is False

        # falls under one of the representation invariants of the survey class
        # unanswered_question_with_same_id = NumericQuestion(0, "No answer!", 1, 2000)
        # assert stu.has_answer(unanswered_question_with_same_id) is False

    def test_unnamed_student(self) -> None:
        with pytest.raises(ValueError):
            stu = Student(0, "")

    def test_general_set_answer(self) -> None:
        stu = Student(0, "Liam")
        question = NumericQuestion(0, "How old are you", 16, 100)
        other_question = YesNoQuestion(1, "Do you have a dog")
        ans = Answer(18)
        stu.set_answer(question, ans)
        assert stu.get_answer(question) is ans
        assert stu.get_answer(other_question) is None

        new_ans = Answer(20)
        stu.set_answer(question, new_ans)
        assert stu.get_answer(question) is new_ans

    def test_replace_answer(self) -> None:
        stu = Student(0, "Liam")
        question = NumericQuestion(0, "How old are you", 16, 100)
        ans = Answer('ten')
        stu.set_answer(question, ans)
        assert stu.get_answer(question) is ans
        new_ans = Answer(50)
        stu.set_answer(question, new_ans)
        assert stu.get_answer(question) is new_ans
        assert len(stu._answers) == 1

    def test_(self) -> None:
        stu = Student(0, "Liam")
        question = NumericQuestion(0, "How old are you", 16, 100)
        ans = Answer('ten')
        stu.set_answer(question, ans)
        assert stu.get_answer(question) is ans
        new_ans = Answer(50)
        stu.set_answer(question, new_ans)
        assert stu.get_answer(question) is new_ans
        assert len(stu._answers) == 1

    def test_general_get_answer(self) -> None:
        stu = Student(0, "Liam")
        question1 = MultipleChoiceQuestion(0, "Dogs or Cats", ['d', 'c'])
        ans1 = Answer('d')
        stu.set_answer(question1, ans1)

        assert stu.get_answer(question1) == ans1

        ans1.content = 'c'
        assert stu.get_answer(question1).content == 'c'

        assert stu.get_answer(Question(1, "No answer")) is None

    def test_get_invalid(self):
        student = Student(0, 'Liam')
        question = NumericQuestion(0, "How old are you", 16, 100)
        ans = Answer('ten')
        student.set_answer(question, ans)
        assert student.get_answer(question) is ans


###############################################################################
# Task 3 Test cases Course class
###############################################################################
class TestCourse:
    def test_general_enroll_students(self) -> None:
        course = Course("CSC148")
        stu_to_enr_1 = list_of_students1[:]
        stu_to_enr_2 = list_of_students_duplicates[:]
        course.enroll_students(stu_to_enr_1)
        for each in course.get_students():
            assert each in stu_to_enr_1

        # if any duplicates enrol none
        course.enroll_students(stu_to_enr_2)
        assert len(course.get_students()) == 6

        course.enroll_students(stu_to_enr_2[0:4])
        assert len(course.get_students()) == 10
        for each in course.get_students():
            assert each in stu_to_enr_1 or each in stu_to_enr_2

        course.enroll_students(list_of_students_same_id)
        assert len(course.get_students()) == 10

        stu_to_enr_1[0] = Student(0, "New Student")
        assert course.get_students()[0] != stu_to_enr_1[0]

        course.enroll_students([Student(200, "Stu1"), Student(200, "Stu1")])
        assert len(course.get_students()) == 10

    def test_course_empty_name(self) -> None:
        with pytest.raises(ValueError):
            course = Course('')

    def test_student_empty_name(self) -> None:
        course = Course('Test')
        assert len(course.get_students()) == 0

        with pytest.raises(ValueError):
            course.enroll_students([Student(0, "")])

    def test_same_student_ids(self):
        course = Course('Test')
        assert len(course.get_students()) == 0

        course.enroll_students([Student(0, "Student1"), Student(0, "Student1")])
        assert len(course.get_students()) == 0

        course.enroll_students([Student(0, "Student1"), Student(1, "Student1")])
        assert len(course.get_students()) == 2

        course.enroll_students([Student(0, "Student1")])
        assert len(course.get_students()) == 2

        course.enroll_students([Student(2, "Student1")])
        assert len(course.get_students()) == 3

    def test_name_already_in_course(self) -> None:
        course = course_with_students(5)
        assert len(course.get_students()) == 5

        course.enroll_students([Student(100, "No Name")])
        assert len(course.get_students()) == 6

    def test_empty_quiz_all_answered(self) -> None:
        course = course_with_students(10)
        survey = Survey([])
        assert course.all_answered(survey) is True

    def test_survey_true(self) -> None:
        course = course_with_students_with_answers(10, generic_questions())
        survey = Survey(generic_questions())
        assert course.all_answered(survey) is True

    def test_no_students_all_answered(self) -> None:
        course = empty_course()
        survey = Survey([NumericQuestion(0, "No question", 0, 10)])
        assert course.all_answered(survey) is True

    def test_general_get_students(self) -> None:
        course = Course("CSC148")

        # assure that it starts empty
        assert course.get_students() == ()
        course.enroll_students(list_of_students1)

        # test ordering
        assert course.get_students() == (
            list_of_students1[5],
            list_of_students1[4],
            list_of_students1[1],
            list_of_students1[3],
            list_of_students1[2],
            list_of_students1[0]
        )


###############################################################################
# Task 4 Test cases QUESTION CLASSES
###############################################################################
class TestQuestion:
    def test_multiple_choice_class_general(self) -> None:
        question = mc_question
        assert question.__str__() == "MC question\nPossible options are: " \
                                     "a, b, c, d, Dog, Cat, Fish, Bird, Hamster"
        good_answer = Answer('a')
        for each in valid_mc_answers:
            assert question.validate_answer(each) is True
        for each in invalid_mc_answers:
            assert question.validate_answer(each) is False
        assert question.get_similarity(good_answer, Answer('b')) == 0.0
        assert question.get_similarity(good_answer, Answer('a')) == 1.0

    def test_get_sim_mc(self) -> None:
        q = MultipleChoiceQuestion(0, "Question", [
            'a', 'b', 'c', 'd', 'e', 'f'])
        assert q.get_similarity(Answer('a'), Answer('a')) == 1.0
        assert q.get_similarity(Answer('a'), Answer('b')) == 0.0
        assert q.get_similarity(Answer('c'), Answer('e')) == 0.0

    def test_numeric_question_general(self) -> None:
        question = num_question
        assert question.__str__() == "Num question\nPossible options are: " \
                                     "Any number between 10 and 100 (inclusive)"
        good_answer = Answer(10)
        for each in valid_num_answers:
            assert question.validate_answer(each) is True
        for each in invalid_num_answers:
            assert question.validate_answer(each) is False
        assert question.get_similarity(good_answer, Answer(55)) == 0.5
        assert question.get_similarity(good_answer, Answer(10)) == 1.0
        assert question.get_similarity(good_answer, Answer(100)) == 0.0

    def test_get_sim_numeric(self) -> None:
        question = NumericQuestion(0, "Question", 0, 100)
        assert question.get_similarity(Answer(0), Answer(100)) == 0
        assert question.get_similarity(Answer(20), Answer(50)) == 0.7
        assert question.get_similarity(Answer(20), Answer(20)) == 1
        assert question.get_similarity(Answer(40), Answer(50)) == 0.9

    def test_yes_or_no_question_general(self) -> None:
        question = yn_question
        assert question.__str__() == "YN question\nPossible options are: " \
                                     "True or False"

        for each in valid_yn_answers:
            assert question.validate_answer(each) is True
        for each in invalid_yn_answers:
            assert question.validate_answer(each) is False

        good_answer = Answer(True)
        good_answer2 = Answer(False)
        assert question.get_similarity(good_answer, good_answer2) == 0.0
        assert question.get_similarity(good_answer, Answer(True)) == 1.0
        assert question.get_similarity(good_answer2, Answer(False)) == 1.0

    def test_get_sim_yn(self) -> None:
        question = YesNoQuestion(0, "Question")
        assert question.get_similarity(Answer(True), Answer(True)) == 1.0
        assert question.get_similarity(Answer(False), Answer(False)) == 1.0
        assert question.get_similarity(Answer(False), Answer(True)) == 0.0
        assert question.get_similarity(Answer(True), Answer(False)) == 0.0


    def test_check_box_question_general(self) -> None:
        question = cb_question
        assert question.__str__() == "CB question\nPossible options are: " \
                                     "a, b, c, d, Dog, Cat, Fish, Bird, Hamster"

        for each in valid_cb_answers:
            assert question.validate_answer(each) is True
        for each in invalid_cb_answers:
            assert question.validate_answer(each) is False

        ans1 = Answer(['Dog', 'Cat'])
        ans2 = Answer(['Fish', 'Bird'])
        assert question.get_similarity(ans1, ans2) == 0.0
        assert question.get_similarity(ans1, Answer(['Dog', 'Cat'])) == 1
        assert question.get_similarity(ans2, Answer(['Dog', 'Bird'])) == 1 / 3

    def test_get_sim_cb(self) -> None:
        q = CheckboxQuestion(0, "Question", ['a', 'b', 'c', 'd', 'e', 'f'])
        assert q.get_similarity(Answer(['a']), Answer(['a'])) == 1.0
        assert q.get_similarity(Answer(['a']), Answer(['b'])) == 0.0
        assert q.get_similarity(Answer(['a', 'b']), Answer(['b', 'c'])) == 1 / 3
        assert q.get_similarity(Answer(['a', 'c', 'e']),
                                Answer(['b', 'd'])) == 0.0
        assert q.get_similarity(Answer(['a', 'b', 'c', 'd', 'e', 'f']),
                                Answer(['b'])) == 1 / 6
        assert q.get_similarity(Answer(['a', 'c', 'd']),
                                Answer(['b', 'c', 'd', 'e'])) == 2 / 5
        assert q.get_similarity(Answer(['a', 'b', 'c']),
                                Answer(['b', 'e', 'a'])) == 2 / 4
        assert q.get_similarity(Answer(['a', 'b', 'c']),
                                Answer(['c', 'b', 'd'])) == 2 / 4


###############################################################################
# Task 5 Test cases ANSWER CLASS
###############################################################################
class TestAnswer:
    def test_is_valid(self) -> None:
        for each in valid_mc_answers:
            assert each.is_valid(mc_question) is True
            assert each.is_valid(num_question) is False
            assert each.is_valid(yn_question) is False
            assert each.is_valid(cb_question) is False
        for each in valid_num_answers:
            assert each.is_valid(mc_question) is False
            assert each.is_valid(num_question) is True
            assert each.is_valid(yn_question) is False
            assert each.is_valid(cb_question) is False
        for each in valid_yn_answers:
            assert each.is_valid(mc_question) is False
            assert each.is_valid(num_question) is False
            assert each.is_valid(yn_question) is True
            assert each.is_valid(cb_question) is False
        for each in valid_cb_answers:
            assert each.is_valid(mc_question) is False
            assert each.is_valid(num_question) is False
            assert each.is_valid(yn_question) is False
            assert each.is_valid(cb_question) is True


###############################################################################
# Task 6 Test cases Criterion
###############################################################################
class TestCriterion:
    def test_homogeneous_general(self) -> None:
        numeric = num_question
        hom = HomogeneousCriterion()
        answers = valid_num_answers
        assert hom.score_answers(numeric, [answers[0]]) == 1
        assert hom.score_answers(numeric, [answers[0], answers[90]]) == 0

        # should approach 2/3 as the number of answers goes to infinity
        assert round(
            hom.score_answers(numeric, answers[2:]), 10) == round(2 / 3, 10)

        for each in invalid_num_answers:
            with pytest.raises(InvalidAnswerError):
                hom.score_answers(numeric, [each])
        with pytest.raises(InvalidAnswerError):
            hom.score_answers(numeric, [Answer("twelve")] + valid_num_answers)

        multiple = mc_question
        answers = valid_mc_answers
        assert hom.score_answers(multiple, [answers[0]]) == 1
        assert hom.score_answers(multiple, [answers[0], answers[1]]) == 0

        # all possible answers are different
        assert hom.score_answers(multiple, answers) == 0

        # two same one different
        answers = [Answer('a'), Answer('b'), Answer('b')]
        assert hom.score_answers(multiple, answers) == 1 / 3

        for each in invalid_mc_answers:
            with pytest.raises(InvalidAnswerError):
                hom.score_answers(multiple, [each])
        with pytest.raises(InvalidAnswerError):
            hom.score_answers(multiple, [Answer("twelve")] + valid_mc_answers)

        yesno = yn_question
        answers = valid_yn_answers
        assert hom.score_answers(yesno, [answers[0]]) == 1
        assert hom.score_answers(yesno, [answers[0], answers[1]]) == 0

        # all possible answers are different
        assert hom.score_answers(yesno, answers) == 0

        # two same one different
        answers = [Answer(True), Answer(False), Answer(True)]
        assert hom.score_answers(yesno, answers) == 1 / 3

        for each in invalid_yn_answers:
            with pytest.raises(InvalidAnswerError):
                hom.score_answers(yesno, [each])
        with pytest.raises(InvalidAnswerError):
            hom.score_answers(yesno, [Answer("twelve")] + valid_yn_answers)

        check = cb_question
        answers = valid_cb_answers
        assert hom.score_answers(check, [answers[0]]) == 1
        assert hom.score_answers(check, [answers[0], answers[1]]) == 0

        # two same one different
        answers = [Answer(['a', 'b']), Answer(['a', 'c']), Answer(['b', 'c'])]
        assert hom.score_answers(check, answers) == 1 / 3

        for each in invalid_cb_answers:
            with pytest.raises(InvalidAnswerError):
                hom.score_answers(check, [each])
        with pytest.raises(InvalidAnswerError):
            hom.score_answers(check, [Answer("twelve")] + valid_cb_answers)

    def test_homo_score_answers(self) -> None:
        # pretty sure this one works
        q = NumericQuestion(0, "Question", 0, 100)
        answers = [Answer(x) for x in range(0, 101, 10)]
        answers2 = [Answer(5), Answer(12), Answer(16), Answer(18)]
        hom = HomogeneousCriterion()
        assert round(hom.score_answers(q, answers), 10) == 0.6
        assert round(hom.score_answers(q, answers2), 6) == 0.928333

        q = MultipleChoiceQuestion(0, "Question", ['a', 'b', 'c', 'd', 'e'])
        answers = [Answer('a'), Answer('b'), Answer('a')]
        assert hom.score_answers(q, answers) == 1 / 3
        answers.append(Answer('b'))
        assert hom.score_answers(q, answers) == 1 / 3
        assert hom.score_answers(q, []) == 0

        q = YesNoQuestion(0, "Question")
        answers = [Answer(True), Answer(False), Answer(False)]
        assert hom.score_answers(q, answers) == 1 / 3

        q = CheckboxQuestion(0, "Question", ['a', 'b', 'c', 'd', 'e'])
        answers = [Answer(['a']), Answer(['b']), Answer(['a'])]
        assert hom.score_answers(q, answers) == 1 / 3
        answers = [Answer(['a', 'b', 'c'])]
        assert hom.score_answers(q, answers) == 1
        answers.append(Answer(['b', 'e', 'a']))
        assert hom.score_answers(q, answers) == 2 / 4
        answers.append(Answer(['b', 'e', 'a']))
        assert hom.score_answers(q, answers) == 2 / 3

        q = NumericQuestion(0, "Test", 1, 6)
        answers = [Answer(3), Answer(2), Answer(3), Answer(3)]
        assert round(hom.score_answers(q, answers), 5) == 0.9

    def test_yes_no_empty_text(self):
        with pytest.raises(ValueError):
            q = YesNoQuestion(0, "")

    def test_mc_empty_text(self):
        with pytest.raises(ValueError):
            q = MultipleChoiceQuestion(0, "", ['a', 'b', 'c', 'd', 'e'])

    def test_num_empty_text(self):
        with pytest.raises(ValueError):
            q = NumericQuestion(0, "", 0, 100)

    def test_check_empty_text(self):
        with pytest.raises(ValueError):
            q = CheckboxQuestion(0, "", ['a', 'b', 'c', 'd', 'e'])

    def test_heterogeneous_general(self) -> None:
        numeric = num_question
        hom = HeterogeneousCriterion()
        answers = valid_num_answers
        assert hom.score_answers(numeric, [answers[0]]) == 0
        assert hom.score_answers(numeric, [answers[0], answers[90]]) == 1

        # should approach 2/3 as the number of answers goes to infinity
        assert round(
            hom.score_answers(numeric, answers[2:]), 10) == round(1 / 3, 10)

        for each in invalid_num_answers:
            with pytest.raises(InvalidAnswerError):
                hom.score_answers(numeric, [each])
        with pytest.raises(InvalidAnswerError):
            hom.score_answers(numeric, [Answer("twelve")] + valid_num_answers)

        multiple = mc_question
        answers = valid_mc_answers
        assert hom.score_answers(multiple, [answers[0]]) == 0
        assert hom.score_answers(multiple, [answers[0], answers[1]]) == 1

        # all possible answers are different
        assert hom.score_answers(multiple, answers) == 1

        # two same one different
        answers = [Answer('a'), Answer('b'), Answer('b')]
        assert round(
            hom.score_answers(multiple, answers), 10) == round(2 / 3, 10)

        for each in invalid_mc_answers:
            with pytest.raises(InvalidAnswerError):
                hom.score_answers(multiple, [each])
        with pytest.raises(InvalidAnswerError):
            hom.score_answers(multiple, [Answer("twelve")] + valid_mc_answers)

        yesno = yn_question
        answers = valid_yn_answers
        assert hom.score_answers(yesno, [answers[0]]) == 0
        assert hom.score_answers(yesno, [answers[0], answers[1]]) == 1

        # all possible answers are different
        assert hom.score_answers(yesno, answers) == 1

        # two same one different
        answers = [Answer(True), Answer(False), Answer(True)]
        assert round(hom.score_answers(yesno, answers), 10) == round(2 / 3, 10)

        for each in invalid_yn_answers:
            with pytest.raises(InvalidAnswerError):
                hom.score_answers(yesno, [each])
        with pytest.raises(InvalidAnswerError):
            hom.score_answers(yesno, [Answer("twelve")] + valid_yn_answers)

        check = cb_question
        answers = valid_cb_answers
        assert hom.score_answers(check, [answers[0]]) == 0
        assert hom.score_answers(check, [answers[0], answers[1]]) == 1

        # two same one different
        answers = [Answer(['a', 'b']), Answer(['a', 'c']), Answer(['b', 'c'])]
        assert round(hom.score_answers(check, answers), 10) == round(2 / 3, 10)

        for each in invalid_cb_answers:
            with pytest.raises(InvalidAnswerError):
                hom.score_answers(check, [each])
        with pytest.raises(InvalidAnswerError):
            hom.score_answers(check, [Answer("twelve")] + valid_cb_answers)

    def test_hetero_score_answers(self) -> None:
        # pretty sure this one works
        q = NumericQuestion(0, "Question", 0, 100)
        answers = [Answer(x) for x in range(0, 101, 10)]
        answers2 = [Answer(5), Answer(12), Answer(16), Answer(18)]
        hom = HeterogeneousCriterion()
        assert round(hom.score_answers(q, answers), 10) == 1 - 0.6
        assert round(
            hom.score_answers(q, answers2), 6) == round(1 - 0.928333, 6)
        q = NumericQuestion(0, "Question", -2, 4)
        assert round(
            hom.score_answers(q, [Answer(0), Answer(-1)]), 5) == round(1 / 6, 5)

    def test_lonely_member(self) -> None:
        numeric = num_question
        hom = LonelyMemberCriterion()
        answers = valid_num_answers
        assert hom.score_answers(numeric, [answers[0]]) == 0
        assert hom.score_answers(numeric, [answers[0], answers[90]]) == 0
        assert hom.score_answers(numeric, answers + answers) == 1

        assert hom.score_answers(numeric, answers) == 0

        for each in invalid_num_answers:
            with pytest.raises(InvalidAnswerError):
                hom.score_answers(numeric, [each])
        with pytest.raises(InvalidAnswerError):
            hom.score_answers(numeric, [Answer("twelve")] + valid_num_answers)

        multiple = mc_question
        answers = valid_mc_answers
        assert hom.score_answers(multiple, [answers[0]]) == 0
        assert hom.score_answers(multiple, answers + answers) == 1

        # all possible answers are different
        assert hom.score_answers(multiple, answers) == 0

        # two same one different
        answers = [Answer('a'), Answer('b'), Answer('b')]
        assert hom.score_answers(multiple, answers) == 0

        for each in invalid_mc_answers:
            with pytest.raises(InvalidAnswerError):
                hom.score_answers(multiple, [each])
        with pytest.raises(InvalidAnswerError):
            hom.score_answers(multiple, [Answer("twelve")] + valid_mc_answers)

        yesno = yn_question
        answers = valid_yn_answers
        assert hom.score_answers(yesno, [answers[0]]) == 0
        assert hom.score_answers(yesno, answers + answers) == 1

        # all possible answers are different
        assert hom.score_answers(yesno, answers) == 0

        # two same one different
        answers = [Answer(True), Answer(False), Answer(True)]
        assert hom.score_answers(yesno, answers) == 0

        for each in invalid_yn_answers:
            with pytest.raises(InvalidAnswerError):
                hom.score_answers(yesno, [each])
        with pytest.raises(InvalidAnswerError):
            hom.score_answers(yesno, [Answer("twelve")] + valid_yn_answers)

        check = cb_question
        answers = valid_cb_answers
        assert hom.score_answers(check, [answers[0]]) == 0
        assert hom.score_answers(check, answers + answers) == 1

        # two same one different
        answers = [Answer(['a', 'b']), Answer(['a', 'c']), Answer(['b', 'c'])]
        assert hom.score_answers(check, answers) == 0

        for each in invalid_cb_answers:
            with pytest.raises(InvalidAnswerError):
                hom.score_answers(check, [each])
        with pytest.raises(InvalidAnswerError):
            hom.score_answers(check, [Answer("twelve")] + valid_cb_answers)


###############################################################################
# Task 7 Test cases Group
###############################################################################
class TestGroup:
    def test_get_members(self) -> None:
        group = Group(list_of_students1)
        members = group.get_members()
        members[0] = Student(100, 'Charlie')
        assert members != group.get_members()
        assert group.get_members() == list_of_students1
        assert group.get_members() is not list_of_students1
        assert len(group) == 6
        assert group.__str__() == 'Liam, Ian, John, Raon, Tina, Zi Qi'
        assert Group([Student(0, 'Liam')]).__str__() == 'Liam'


###############################################################################
# Task 8 Test cases Grouping
###############################################################################
class TestGrouping:
    def test_groups_length(self) -> None:
        groups = Grouping()
        assert len(groups) == 0
        groups.add_group(group_norm)
        assert len(groups) == 1
        groups.add_group(group_norm2)
        assert len(groups) == 2
        groups.add_group(group_duplicates)
        assert len(groups) == 2

    def test_str_method_group(self) -> None:
        groups = Grouping()
        assert groups.__str__() == ""
        groups.add_group(group_norm)
        assert groups.__str__() == group_norm.__str__()
        groups.add_group(group_norm2)
        assert groups.__str__() == \
               group_norm.__str__() + '\n' + group_norm2.__str__()

    def test_add_group(self) -> None:
        groups = Grouping()
        assert groups.add_group(group_norm) is True
        assert groups.add_group(group_norm2) is True
        assert groups.add_group(group_duplicates) is False
        assert groups.add_group(group_one) is True

    def test_get_groups(self) -> None:
        groups = Grouping()
        assert groups.get_groups() == []
        groups.add_group(group_norm)
        assert groups.get_groups() == [group_norm]
        groups.add_group(group_norm2)
        assert groups.get_groups() == [group_norm, group_norm2]
        groups.add_group(group_duplicates)
        assert groups.get_groups() == [group_norm, group_norm2]

        # assure it is shallow copied
        edit_groups = groups.get_groups()
        edit_groups[0] = group_one
        assert groups.get_groups() == [group_norm, group_norm2]
        assert groups.get_groups() != edit_groups


###############################################################################
# Task 9 Test cases Survey Class
###############################################################################
class TestSurvey:
    def test_len_survey(self) -> None:
        survey = Survey(list_of_questions_empty)
        assert len(survey) == 0

        survey2 = Survey(list_of_questions1)
        assert len(survey2) == len(list_of_questions1)
        assert Question(0, "None") in survey2

    def test_in_survey(self) -> None:
        survey = Survey(list_of_questions1)
        assert Question(0, "None") in survey

        survey2 = Survey(list_of_questions1 + list_of_questions2)
        for each in list_of_questions_used_ids_new_types:
            assert each in survey2

        for each in list_of_questions_same_questions_diff_id:
            assert each not in survey2

    def test_str_survey(self) -> None:
        survey = Survey(list_of_questions1)
        string = "Questions:"
        for q in list_of_questions1:
            string += "\n" + q.__str__() + "\n"
            string += f"Criteria: {type(survey._get_criterion(q))}\n"
            string += f"Weight: {survey._get_weight(q)}\n"
        assert survey.__str__() == string

    def test_get_questions(self) -> None:
        survey = Survey(list_of_questions1)
        assert survey.get_questions() == list_of_questions1
        shallow_copy_list = survey.get_questions()
        shallow_copy_list[0] = Question(100, "NONE")
        assert survey.get_questions() == list_of_questions1
        assert survey.get_questions() != shallow_copy_list

    def test__get_criterion(self) -> None:
        survey = Survey(list_of_questions1)
        for each in survey.get_questions():
            assert type(survey._get_criterion(each)) is HomogeneousCriterion

    def test__get_weight(self) -> None:
        survey = Survey(list_of_questions1)
        for each in list_of_questions1:
            assert survey._get_weight(each) == 1

    def test_set_weight(self) -> None:
        survey = Survey(list_of_questions1)
        for each in list_of_questions1:
            assert survey._get_weight(each) == 1

        assert survey.set_weight(5, list_of_questions1[0]) is True
        assert survey._get_weight(list_of_questions1[0]) == 5

        assert survey.set_weight(5, Question(100, "NONE")) is False

    def test_set_criterion(self) -> None:
        survey = Survey(list_of_questions1)
        for each in list_of_questions1:
            assert type(survey._get_criterion(each)) is HomogeneousCriterion

        assert survey.set_criterion(HeterogeneousCriterion(),
                                    list_of_questions1[0]) is True
        assert type(survey._get_criterion(list_of_questions1[0])) \
               is HeterogeneousCriterion
        assert type(survey._get_criterion(list_of_questions1[0])) \
               is not Criterion

        assert survey.set_criterion(HeterogeneousCriterion,
                                    Question(100, "NONE")) is False

    def test_score_students(self) -> None:
        survey_empty = Survey(list_of_questions_empty)
        assert survey_empty.score_students(list_of_students1) == 0

        survey = Survey(list_of_questions1)
        # these students have no answers
        assert survey.score_students(list_of_students1) == 0

        survey_short = Survey([YesNoQuestion(0, "YN"), YesNoQuestion(1, "YN2")])
        for each in list_of_students1:
            each.set_answer(survey_short.get_questions()[0], Answer(True))
            each.set_answer(survey_short.get_questions()[1], Answer(False))

        assert survey_short.score_students(list_of_students1) == 1

        given_survey = Survey([given_questions[0]])
        assert round(given_survey.score_students(given_stu1), 5) == 0.9

    def test_pre_made_test_score_grouping(self) -> None:
        questions = [MultipleChoiceQuestion(1, 'why?', ['a', 'b']),
                     NumericQuestion(2, 'what?', -2, 4),
                     YesNoQuestion(3, 'really?'),
                     CheckboxQuestion(4, 'how?', ['a', 'b', 'c'])]
        criteria = [HomogeneousCriterion(),
                    HeterogeneousCriterion(),
                    LonelyMemberCriterion(),
                    HomogeneousCriterion()]
        weights = [2, 5, 7, 4]
        answers = [[Answer('a'), Answer('b'), Answer('a'), Answer('b')],
                   [Answer(0), Answer(4), Answer(-1), Answer(1)],
                   [Answer(True), Answer(False), Answer(True), Answer(True)],
                   [Answer(['a', 'b']), Answer(['a', 'b']),
                    Answer(['a']), Answer(['b'])]]

        course_with_students = Course('csc148')
        students = [Student(1, 'Zoro'),
                    Student(2, 'Aaron'),
                    Student(3, 'Gertrude'),
                    Student(4, 'Yvette')]
        course_with_students.enroll_students(students)

        s = Survey(questions)
        for i, question in enumerate(questions):
            s.set_weight(weights[i], question)
            s.set_criterion(criteria[i], question)
        survey_ = s

        students = course_with_students.get_students()

        students_with_answers = students
        for i, student in enumerate(students):
            for j, question in enumerate(questions):
                student.set_answer(question, answers[j][i])

        greedy_grouping = Grouping()
        greedy_grouping.add_group(Group([students_with_answers[1],
                                         students_with_answers[3]]))
        greedy_grouping.add_group(Group([students_with_answers[0],
                                         students_with_answers[2]]))

        print()
        for group in greedy_grouping.get_groups():
            for i, q in enumerate(questions):
                for stu in group.get_members():
                    print(stu.get_answer(q).content, end=', ')
                print(survey_.score_students(group.get_members()))
                print(type(survey_._get_criterion(q)),
                      f"{survey_._get_weight(q)}\n")

        score = survey_.score_grouping(greedy_grouping)
        assert round(score, 2) == 2.29


###############################################################################
# Task 10 Test cases GROUPERS
###############################################################################
class TestGroupers:
    def test_alpha_make_grouping_general(self) -> None:
        alpha = AlphaGrouper(2)
        survey_short = main_survey_short
        course = Course("Test")
        course.enroll_students(list_of_students1_with_answers)

        grouping = alpha.make_grouping(course, survey_short)
        expected_grouping = Grouping()
        expected_grouping.add_group(Group(list_of_students1_with_answers[1:2] +
                                          list_of_students1_with_answers[2:3]))
        expected_grouping.add_group(Group(list_of_students1_with_answers[0:1] +
                                          list_of_students1_with_answers[3:4]))
        expected_grouping.add_group(Group(list_of_students1_with_answers[4:5] +
                                          list_of_students1_with_answers[5:]))

        assert len(grouping.get_groups()) == 3
        for i in range(3):
            assert grouping.get_groups()[i].get_members() == \
                   expected_grouping.get_groups()[i].get_members()

    def test_alpha_multiple_same_names(self) -> None:
        alpha = AlphaGrouper(2)
        survey_short = main_survey_short

        students = [Student(0, "Liam"), Student(1, "Liam"),
                    Student(3, "A"), Student(2, "A")]
        course = Course("Test")
        course.enroll_students(students)

        expected_grouping = Grouping()
        expected_grouping.add_group(Group([students[3], students[2]]))
        expected_grouping.add_group(Group(students[0:2]))

        grouping = alpha.make_grouping(course, survey_short)

        assert len(grouping.get_groups()) == 2
        for i in range(2):
            print(grouping.get_groups()[i].get_members(), ", ",
                  expected_grouping.get_groups()[i].get_members())

            assert grouping.get_groups()[i].get_members() == \
                   expected_grouping.get_groups()[i].get_members()

    def test_greedy(self) -> None:
        greedy = GreedyGrouper(2)
        survey_short = main_survey_short
        course = course_with_students_with_set_answers(
            survey_short.get_questions())
        students = course.get_students()

        grouping = greedy.make_grouping(course, survey_short)
        expected_grouping = Grouping()
        expected_grouping.add_group(Group([students[0], students[2]]))
        expected_grouping.add_group(Group([students[1], students[3]]))
        expected_grouping.add_group(Group([students[4]]))

        assert len(grouping.get_groups()) == 3
        for i in range(3):
            assert grouping.get_groups()[i].get_members() == \
                   expected_grouping.get_groups()[i].get_members()

    def test_simulated_annealing(self) -> None:
        simu = SimulatedAnnealingGrouper(2, 1000, 10)
        survey_short = main_survey_short
        course = course_with_students_with_set_answers(
            survey_short.get_questions())
        students = course.get_students()

        grouping = simu.make_grouping(course, survey_short)
        expected_grouping = Grouping()
        expected_grouping.add_group(Group([students[0], students[2]]))
        expected_grouping.add_group(Group([students[1], students[3]]))
        expected_grouping.add_group(Group([students[4]]))

        assert len(grouping.get_groups()) == 3
        lst1 = []
        for each in grouping.get_groups():
            lst1.append(each.get_members())
        lst2 = []
        for each in expected_grouping.get_groups():
            lst2.append(each.get_members())

        assert total_score(survey_short, lst1) == \
               total_score(survey_short, lst2)

    def test_group_contains(self) -> None:
        num = 10
        group = Group(list(course_with_students(num).get_students()))
        for i in range(0, num):
            assert Student(i, "NONE") in group


if __name__ == '__main__':
    pytest.main(['example_tests.py'])
