import unittest
import sys
import os
import importlib

# 将项目根目录添加到系统路径以支持模块导入
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 使用 importlib 动态导入所有含数字前缀的 Solution 类与数据结构类
TwoSumSolution = importlib.import_module("arrays.01_two_sum").Solution
MaxProfitSolution = importlib.import_module("arrays.02_best_time_to_buy_and_sell_stock").Solution
ContainsDuplicateSolution = importlib.import_module("arrays.03_contains_duplicate").Solution
ProductExceptSelfSolution = importlib.import_module("arrays.04_product_of_array_except_self").Solution
MaxSubArraySolution = importlib.import_module("arrays.05_maximum_subarray").Solution
MaxProductSolution = importlib.import_module("arrays.06_maximum_product_subarray").Solution
FindMinSolution = importlib.import_module("arrays.07_find_minimum_in_rotated_sorted_array").Solution
SearchSolution = importlib.import_module("arrays.08_search_in_rotated_sorted_array").Solution
ThreeSumSolution = importlib.import_module("arrays.09_three_sum").Solution
MaxAreaSolution = importlib.import_module("arrays.10_container_with_most_water").Solution

GetSumSolution = importlib.import_module("binary.11_sum_of_two_integers").Solution
HammingWeightSolution = importlib.import_module("binary.12_number_of_1_bits").Solution
CountBitsSolution = importlib.import_module("binary.13_counting_bits").Solution
MissingNumberSolution = importlib.import_module("binary.14_missing_number").Solution
ReverseBitsSolution = importlib.import_module("binary.15_reverse_bits").Solution

ClimbStairsSolution = importlib.import_module("dynamic_programming.16_climbing_stairs").Solution
CoinChangeSolution = importlib.import_module("dynamic_programming.17_coin_change").Solution
LengthOfLISSolution = importlib.import_module("dynamic_programming.18_longest_increasing_subsequence").Solution
LongestCommonSubsequenceSolution = importlib.import_module("dynamic_programming.19_longest_common_subsequence").Solution
WordBreakSolution = importlib.import_module("dynamic_programming.20_word_break").Solution
CombinationSum4Solution = importlib.import_module("dynamic_programming.21_combination_sum_iv").Solution
RobSolution = importlib.import_module("dynamic_programming.22_house_robber").Solution
Rob2Solution = importlib.import_module("dynamic_programming.23_house_robber_ii").Solution
NumDecodingsSolution = importlib.import_module("dynamic_programming.24_decode_ways").Solution
UniquePathsSolution = importlib.import_module("dynamic_programming.25_unique_paths").Solution
CanJumpSolution = importlib.import_module("dynamic_programming.26_jump_game").Solution

CloneGraphSolution = importlib.import_module("graph.27_clone_graph").Solution
GraphNode = importlib.import_module("graph.27_clone_graph").Node
CanFinishSolution = importlib.import_module("graph.28_course_schedule").Solution
PacificAtlanticSolution = importlib.import_module("graph.29_pacific_atlantic_water_flow").Solution
NumIslandsSolution = importlib.import_module("graph.30_number_of_islands").Solution
LongestConsecutiveSolution = importlib.import_module("graph.31_longest_consecutive_sequence").Solution
AlienOrderSolution = importlib.import_module("graph.32_alien_dictionary").Solution
ValidTreeSolution = importlib.import_module("graph.33_graph_valid_tree").Solution
CountComponentsSolution = importlib.import_module("graph.34_number_of_connected_components_in_an_undirected_graph").Solution

InsertSolution = importlib.import_module("interval.35_insert_interval").Solution
MergeSolution = importlib.import_module("interval.36_merge_intervals").Solution
EraseOverlapIntervalsSolution = importlib.import_module("interval.37_non_overlapping_intervals").Solution
CanAttendMeetingsSolution = importlib.import_module("interval.38_meeting_rooms").Solution
MinMeetingRoomsSolution = importlib.import_module("interval.39_meeting_rooms_ii").Solution

ReverseListSolution = importlib.import_module("linked_list.40_reverse_linked_list").Solution
ListNode = importlib.import_module("linked_list.40_reverse_linked_list").ListNode
HasCycleSolution = importlib.import_module("linked_list.41_linked_list_cycle").Solution
MergeTwoListsSolution = importlib.import_module("linked_list.42_merge_two_sorted_lists").Solution
MergeKListsSolution = importlib.import_module("linked_list.43_merge_k_sorted_lists").Solution
RemoveNthFromEndSolution = importlib.import_module("linked_list.44_remove_nth_node_from_end_of_list").Solution
ReorderListSolution = importlib.import_module("linked_list.45_reorder_list").Solution

SetZeroesSolution = importlib.import_module("matrix.46_set_matrix_zeroes").Solution
SpiralOrderSolution = importlib.import_module("matrix.47_spiral_matrix").Solution
RotateSolution = importlib.import_module("matrix.48_rotate_image").Solution
ExistSolution = importlib.import_module("matrix.49_word_search").Solution

LengthOfLongestSubstringSolution = importlib.import_module("strings.50_longest_substring_without_repeating_characters").Solution
CharacterReplacementSolution = importlib.import_module("strings.51_longest_repeating_character_replacement").Solution
MinWindowSolution = importlib.import_module("strings.52_minimum_window_substring").Solution
IsAnagramSolution = importlib.import_module("strings.53_valid_anagram").Solution
GroupAnagramsSolution = importlib.import_module("strings.54_group_anagrams").Solution
IsValidSolution = importlib.import_module("strings.55_valid_parentheses").Solution
IsPalindromeSolution = importlib.import_module("strings.56_valid_palindrome").Solution
LongestPalindromeSolution = importlib.import_module("strings.57_longest_palindromic_substring").Solution
CountSubstringsSolution = importlib.import_module("strings.58_palindromic_substrings").Solution
EncodeDecodeCodec = importlib.import_module("strings.59_encode_and_decode_strings").Codec

MaxDepthSolution = importlib.import_module("tree.60_maximum_depth_of_binary_tree").Solution
TreeNode = importlib.import_module("tree.60_maximum_depth_of_binary_tree").TreeNode
IsSameTreeSolution = importlib.import_module("tree.61_same_tree").Solution
InvertTreeSolution = importlib.import_module("tree.62_invert_binary_tree").Solution
MaxPathSumSolution = importlib.import_module("tree.63_binary_tree_maximum_path_sum").Solution
LevelOrderSolution = importlib.import_module("tree.64_binary_tree_level_order_traversal").Solution
SerializeDeserializeCodec = importlib.import_module("tree.65_serialize_and_deserialize_binary_tree").Codec
IsSubtreeSolution = importlib.import_module("tree.66_subtree_of_another_tree").Solution
BuildTreeSolution = importlib.import_module("tree.67_construct_binary_tree_from_preorder_and_inorder_traversal").Solution
IsValidBSTSolution = importlib.import_module("tree.68_validate_binary_search_tree").Solution
KthSmallestSolution = importlib.import_module("tree.69_kth_smallest_element_in_a_bst").Solution
LowestCommonAncestorSolution = importlib.import_module("tree.70_lowest_common_ancestor_of_a_binary_search_tree").Solution
TrieSolution = importlib.import_module("tree.71_implement_trie_prefix_tree").Trie
WordDictionarySolution = importlib.import_module("tree.72_add_and_search_word_data_structure_design").WordDictionary
FindWordsSolution = importlib.import_module("tree.73_word_search_ii").Solution

TopKFrequentSolution = importlib.import_module("heap.74_top_k_frequent_elements").Solution
MedianFinderSolution = importlib.import_module("heap.75_find_median_from_data_stream").MedianFinder

class TestBlind75(unittest.TestCase):

    # --- Array Tests ---
    def test_01_two_sum(self):
        s = TwoSumSolution()
        self.assertEqual(s.twoSum([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(s.twoSum([3, 2, 4], 6), [1, 2])

    def test_02_max_profit(self):
        s = MaxProfitSolution()
        self.assertEqual(s.maxProfit([7, 1, 5, 3, 6, 4]), 5)
        self.assertEqual(s.maxProfit([7, 6, 4, 3, 1]), 0)

    def test_03_contains_duplicate(self):
        s = ContainsDuplicateSolution()
        self.assertTrue(s.containsDuplicate([1, 2, 3, 1]))
        self.assertFalse(s.containsDuplicate([1, 2, 3, 4]))

    def test_04_product_except_self(self):
        s = ProductExceptSelfSolution()
        self.assertEqual(s.productExceptSelf([1, 2, 3, 4]), [24, 12, 8, 6])

    def test_05_max_subarray(self):
        s = MaxSubArraySolution()
        self.assertEqual(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)

    def test_06_max_product(self):
        s = MaxProductSolution()
        self.assertEqual(s.maxProduct([2, 3, -2, 4]), 6)

    def test_07_find_min(self):
        s = FindMinSolution()
        self.assertEqual(s.findMin([3, 4, 5, 1, 2]), 1)

    def test_08_search(self):
        s = SearchSolution()
        self.assertEqual(s.search([4, 5, 6, 7, 0, 1, 2], 0), 4)
        self.assertEqual(s.search([4, 5, 6, 7, 0, 1, 2], 3), -1)

    def test_09_three_sum(self):
        s = ThreeSumSolution()
        self.assertEqual(s.threeSum([-1, 0, 1, 2, -1, -4]), [[-1, -1, 2], [-1, 0, 1]])

    def test_10_max_area(self):
        s = MaxAreaSolution()
        self.assertEqual(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)

    # --- Binary Tests ---
    def test_11_get_sum(self):
        s = GetSumSolution()
        self.assertEqual(s.getSum(1, 2), 3)

    def test_12_hamming_weight(self):
        s = HammingWeightSolution()
        self.assertEqual(s.hammingWeight(11), 3)  # 11 is 1011 in binary

    def test_13_count_bits(self):
        s = CountBitsSolution()
        self.assertEqual(s.countBits(2), [0, 1, 1])

    def test_14_missing_number(self):
        s = MissingNumberSolution()
        self.assertEqual(s.missingNumber([3, 0, 1]), 2)

    def test_15_reverse_bits(self):
        s = ReverseBitsSolution()
        self.assertEqual(s.reverseBits(43261596), 964176192)

    # --- DP Tests ---
    def test_16_climb_stairs(self):
        s = ClimbStairsSolution()
        self.assertEqual(s.climbStairs(2), 2)
        self.assertEqual(s.climbStairs(3), 3)

    def test_17_coin_change(self):
        s = CoinChangeSolution()
        self.assertEqual(s.coinChange([1, 2, 5], 11), 3)

    def test_18_length_of_lis(self):
        s = LengthOfLISSolution()
        self.assertEqual(s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]), 4)

    def test_19_longest_common_subsequence(self):
        s = LongestCommonSubsequenceSolution()
        self.assertEqual(s.longestCommonSubsequence("abcde", "ace"), 3)

    def test_20_word_break(self):
        s = WordBreakSolution()
        self.assertTrue(s.wordBreak("leetcode", ["leet", "code"]))

    def test_21_combination_sum_4(self):
        s = CombinationSum4Solution()
        self.assertEqual(s.combinationSum4([1, 2, 3], 4), 7)

    def test_22_rob(self):
        s = RobSolution()
        self.assertEqual(s.rob([1, 2, 3, 1]), 4)

    def test_23_rob2(self):
        s = Rob2Solution()
        self.assertEqual(s.rob([2, 3, 2]), 3)

    def test_24_num_decodings(self):
        s = NumDecodingsSolution()
        self.assertEqual(s.numDecodings("12"), 2)

    def test_25_unique_paths(self):
        s = UniquePathsSolution()
        self.assertEqual(s.uniquePaths(3, 7), 28)

    def test_26_can_jump(self):
        s = CanJumpSolution()
        self.assertTrue(s.canJump([2, 3, 1, 1, 4]))
        self.assertFalse(s.canJump([3, 2, 1, 0, 4]))

    # --- Graph Tests ---
    def test_27_clone_graph(self):
        # 简单克隆测试，这里仅检验空或单个节点
        s = CloneGraphSolution()
        self.assertIsNone(s.cloneGraph(None))
        node = GraphNode(1)
        cloned = s.cloneGraph(node)
        self.assertEqual(cloned.val, 1)

    def test_28_can_finish(self):
        s = CanFinishSolution()
        self.assertTrue(s.canFinish(2, [[1, 0]]))
        self.assertFalse(s.canFinish(2, [[1, 0], [0, 1]]))

    def test_29_pacific_atlantic(self):
        s = PacificAtlanticSolution()
        heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
        # 验证返回的结果是列表并且不为空
        self.assertTrue(len(s.pacificAtlantic(heights)) > 0)

    def test_30_num_islands(self):
        s = NumIslandsSolution()
        grid = [
          ["1","1","1","1","0"],
          ["1","1","0","1","0"],
          ["1","1","0","0","0"],
          ["0","0","0","0","0"]
        ]
        self.assertEqual(s.numIslands(grid), 1)

    def test_31_longest_consecutive(self):
        s = LongestConsecutiveSolution()
        self.assertEqual(s.longestConsecutive([100, 4, 200, 1, 3, 2]), 4)

    def test_32_alien_order(self):
        s = AlienOrderSolution()
        self.assertEqual(s.alienOrder(["wrt","wrf","er","ett","rftt"]), "wertf")

    def test_33_valid_tree(self):
        s = ValidTreeSolution()
        self.assertTrue(s.validTree(5, [[0,1], [0,2], [0,3], [1,4]]))
        self.assertFalse(s.validTree(5, [[0,1], [1,2], [2,3], [1,3], [1,4]]))

    def test_34_count_components(self):
        s = CountComponentsSolution()
        self.assertEqual(s.countComponents(5, [[0,1], [1,2], [3,4]]), 2)

    # --- Interval Tests ---
    def test_35_insert_interval(self):
        s = InsertSolution()
        self.assertEqual(s.insert([[1,3],[6,9]], [2,5]), [[1,5],[6,9]])

    def test_36_merge_intervals(self):
        s = MergeSolution()
        self.assertEqual(s.merge([[1,3],[2,6],[8,10],[15,18]]), [[1,6],[8,10],[15,18]])

    def test_37_erase_overlap_intervals(self):
        s = EraseOverlapIntervalsSolution()
        self.assertEqual(s.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]), 1)

    def test_38_can_attend_meetings(self):
        s = CanAttendMeetingsSolution()
        self.assertFalse(s.canAttendMeetings([[0,30],[5,10],[15,20]]))
        self.assertTrue(s.canAttendMeetings([[7,10],[2,4]]))

    def test_39_min_meeting_rooms(self):
        s = MinMeetingRoomsSolution()
        self.assertEqual(s.minMeetingRooms([[0,30],[5,10],[15,20]]), 2)

    # --- Linked List Tests ---
    def test_40_reverse_list(self):
        s = ReverseListSolution()
        head = ListNode(1, ListNode(2))
        rev = s.reverseList(head)
        self.assertEqual(rev.val, 2)
        self.assertEqual(rev.next.val, 1)

    def test_41_has_cycle(self):
        s = HasCycleSolution()
        head = ListNode(1)
        self.assertFalse(s.hasCycle(head))

    def test_42_merge_two_lists(self):
        s = MergeTwoListsSolution()
        l1 = ListNode(1, ListNode(3))
        l2 = ListNode(2, ListNode(4))
        merged = s.mergeTwoLists(l1, l2)
        self.assertEqual(merged.val, 1)
        self.assertEqual(merged.next.val, 2)

    def test_43_merge_k_lists(self):
        s = MergeKListsSolution()
        l1 = ListNode(1, ListNode(4))
        l2 = ListNode(2, ListNode(3))
        merged = s.mergeKLists([l1, l2])
        self.assertEqual(merged.val, 1)
        self.assertEqual(merged.next.val, 2)

    def test_44_remove_nth_from_end(self):
        s = RemoveNthFromEndSolution()
        head = ListNode(1, ListNode(2, ListNode(3)))
        res = s.removeNthFromEnd(head, 2) # deletes 2, yields 1 -> 3
        self.assertEqual(res.val, 1)
        self.assertEqual(res.next.val, 3)

    def test_45_reorder_list(self):
        s = ReorderListSolution()
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
        s.reorderList(head) # 1 -> 4 -> 2 -> 3
        self.assertEqual(head.val, 1)
        self.assertEqual(head.next.val, 4)
        self.assertEqual(head.next.next.val, 2)

    # --- Matrix Tests ---
    def test_46_set_zeroes(self):
        s = SetZeroesSolution()
        matrix = [[1,1,1],[1,0,1],[1,1,1]]
        s.setZeroes(matrix)
        self.assertEqual(matrix, [[1,0,1],[0,0,0],[1,0,1]])

    def test_47_spiral_order(self):
        s = SpiralOrderSolution()
        self.assertEqual(s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]), [1,2,3,6,9,8,7,4,5])

    def test_48_rotate_image(self):
        s = RotateSolution()
        matrix = [[1,2],[3,4]]
        s.rotate(matrix)
        self.assertEqual(matrix, [[3,1],[4,2]])

    def test_49_word_search(self):
        s = ExistSolution()
        board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
        self.assertTrue(s.exist(board, "ABCCED"))

    # --- String Tests ---
    def test_50_length_of_longest_substring(self):
        s = LengthOfLongestSubstringSolution()
        self.assertEqual(s.lengthOfLongestSubstring("abcabcbb"), 3)

    def test_51_character_replacement(self):
        s = CharacterReplacementSolution()
        self.assertEqual(s.characterReplacement("ABAB", 2), 4)

    def test_52_min_window(self):
        s = MinWindowSolution()
        self.assertEqual(s.minWindow("ADOBECODEBANC", "ABC"), "BANC")

    def test_53_is_anagram(self):
        s = IsAnagramSolution()
        self.assertTrue(s.isAnagram("anagram", "nagaram"))

    def test_54_group_anagrams(self):
        s = GroupAnagramsSolution()
        res = s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        self.assertEqual(len(res), 3)

    def test_55_is_valid(self):
        s = IsValidSolution()
        self.assertTrue(s.isValid("()[]{}"))
        self.assertFalse(s.isValid("(]"))

    def test_56_is_palindrome(self):
        s = IsPalindromeSolution()
        self.assertTrue(s.isPalindrome("A man, a plan, a canal: Panama"))

    def test_57_longest_palindrome(self):
        s = LongestPalindromeSolution()
        self.assertEqual(s.longestPalindrome("babad"), "bab") # or "aba"

    def test_58_count_substrings(self):
        s = CountSubstringsSolution()
        self.assertEqual(s.countSubstrings("abc"), 3)
        self.assertEqual(s.countSubstrings("aaa"), 6)

    def test_59_encode_decode(self):
        c = EncodeDecodeCodec()
        original = ["hello", "world", "ab#c"]
        encoded = c.encode(original)
        decoded = c.decode(encoded)
        self.assertEqual(decoded, original)

    # --- Tree Tests ---
    def test_60_max_depth(self):
        s = MaxDepthSolution()
        root = TreeNode(3, TreeNode(9), TreeNode(20))
        self.assertEqual(s.maxDepth(root), 2)

    def test_61_is_same_tree(self):
        s = IsSameTreeSolution()
        p = TreeNode(1, TreeNode(2))
        q = TreeNode(1, TreeNode(2))
        self.assertTrue(s.isSameTree(p, q))

    def test_62_invert_tree(self):
        s = InvertTreeSolution()
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        inverted = s.invertTree(root)
        self.assertEqual(inverted.left.val, 3)
        self.assertEqual(inverted.right.val, 2)

    def test_63_max_path_sum(self):
        s = MaxPathSumSolution()
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        self.assertEqual(s.maxPathSum(root), 6)

    def test_64_level_order(self):
        s = LevelOrderSolution()
        root = TreeNode(3, TreeNode(9), TreeNode(20))
        self.assertEqual(s.levelOrder(root), [[3], [9, 20]])

    def test_65_serialize_deserialize(self):
        c = SerializeDeserializeCodec()
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        serialized = c.serialize(root)
        deserialized = c.deserialize(serialized)
        self.assertEqual(deserialized.val, 1)
        self.assertEqual(deserialized.left.val, 2)
        self.assertEqual(deserialized.right.val, 3)

    def test_66_is_subtree(self):
        s = IsSubtreeSolution()
        r = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
        sub = TreeNode(4, TreeNode(1), TreeNode(2))
        self.assertTrue(s.isSubtree(r, sub))

    def test_67_build_tree(self):
        s = BuildTreeSolution()
        preorder = [3,9,20,15,7]
        inorder = [9,3,15,20,7]
        root = s.buildTree(preorder, inorder)
        self.assertEqual(root.val, 3)

    def test_68_is_valid_bst(self):
        s = IsValidBSTSolution()
        root = TreeNode(2, TreeNode(1), TreeNode(3))
        self.assertTrue(s.isValidBST(root))

    def test_69_kth_smallest(self):
        s = KthSmallestSolution()
        root = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
        self.assertEqual(s.kthSmallest(root, 1), 1)

    def test_70_lowest_common_ancestor(self):
        s = LowestCommonAncestorSolution()
        p = TreeNode(2)
        q = TreeNode(8)
        root = TreeNode(6, p, q)
        self.assertEqual(s.lowestCommonAncestor(root, p, q).val, 6)

    def test_71_trie(self):
        t = TrieSolution()
        t.insert("apple")
        self.assertTrue(t.search("apple"))
        self.assertFalse(t.search("app"))
        self.assertTrue(t.startsWith("app"))

    def test_72_word_dictionary(self):
        wd = WordDictionarySolution()
        wd.addWord("bad")
        wd.addWord("dad")
        self.assertTrue(wd.search(".ad"))
        self.assertFalse(wd.search("pad"))

    def test_73_find_words(self):
        s = FindWordsSolution()
        board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
        words = ["oath","pea","eat","rain"]
        self.assertEqual(s.findWords(board, words), ["oath", "eat"])

    # --- Heap Tests ---
    def test_74_top_k_frequent(self):
        s = TopKFrequentSolution()
        self.assertEqual(s.topKFrequent([1,1,1,2,2,3], 2), [1, 2])

    def test_75_median_finder(self):
        mf = MedianFinderSolution()
        mf.addNum(1)
        mf.addNum(2)
        self.assertEqual(mf.findMedian(), 1.5)
        mf.addNum(3)
        self.assertEqual(mf.findMedian(), 2.0)

if __name__ == '__main__':
    unittest.main()
