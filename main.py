from grading_tests import GradingTests

gt = GradingTests()

res_list = gt.delete_all_with_hashtag()
for r in res_list:
    print(r)
