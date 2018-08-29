from grading_tests import GradingTests

gt = GradingTests()

res_list = gt.get_all_normal_count()
for r in res_list:
    print(r)
