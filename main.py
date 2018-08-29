from grading_tests import GradingTests

gt = GradingTests()

res_list = gt.get_all_with_hashtag()
for r in res_list:
    print(r)
