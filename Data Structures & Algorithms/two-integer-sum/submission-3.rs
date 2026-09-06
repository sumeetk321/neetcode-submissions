impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut m = HashMap::new();

        for i in 0..nums.len() {
            if let Some(val) = m.get(&(target-nums[i])) {
                return vec![ *val as i32, i as i32];
            }
            m.entry(&nums[i]).or_insert(i);
        }
        vec![0]
    }
}
