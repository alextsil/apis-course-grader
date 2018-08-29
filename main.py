from grading_tests import GradingTests

gt = GradingTests()

res_list = gt.get_all_greater_than()
for r in res_list:
    print(r)
