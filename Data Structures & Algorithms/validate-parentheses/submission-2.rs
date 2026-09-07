impl Solution {
    pub fn is_valid(s: String) -> bool {
        let mut st = Vec::new();
        let close_to_open: HashMap<char, char> =
            [(')', '('), (']', '['), ('}', '{')].into();
        for ch in s.chars() {
            if let Some(&open) = close_to_open.get(&ch) {
                if st.last() == Some(&open) {
                    st.pop();
                } else {
                    return false;
                }
            } else {
                st.push(ch);
            }
        }
        st.is_empty()
    }
}
