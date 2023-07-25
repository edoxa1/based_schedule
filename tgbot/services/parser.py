from py_pdf_parser.loaders import load_file


document = load_file("schedule.pdf")
# start = document.get_page(1).document.elements.filter_by_text_contains("Abbr").extract_single_element()
# for course in end:
#     print(course.text())
# end = document.get_page(1).document.elements.vertically_in_line_with(start)

courses = []

abbreviation_column_start = document.elements.filter_by_text_contains("Abbr").extract_single_element()
abbreviation_column_end = document.elements.vertically_in_line_with(abbreviation_column_start, all_pages=True)


for c in abbreviation_column_end:
    course_line_start = document.elements.filter_by_text_equal(c.text()).extract_single_element()
    course_line_end = document.elements.horizontally_in_line_with(course_line_start)
    print(c.text(), "|", end="")
    for course in course_line_end:
        print(course.text().replace('\n', ' '), end="|")

    print("\n---------------")
