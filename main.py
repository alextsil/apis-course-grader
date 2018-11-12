from grading_tests import GradingTests
from logger import Logger

logger = Logger().logger

gt = GradingTests()
res_list = []

res_list.extend(gt.get_all_normal_count())
res_list.extend(gt.get_all_greater_than())
res_list.extend(gt.get_all_with_hashtag())
res_list.extend(gt.delete_all_with_hashtag())
res_list.extend(gt.simple_post())

true_count = 0
for r in res_list:
    print(r)
    if r.result:
        true_count += 1

print("Passed tests: " + str(true_count) + '/' + str(len(res_list)))
