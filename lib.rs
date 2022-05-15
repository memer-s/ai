mod types;

#[cfg(test)]
mod tests {
    use crate::types;

    #[test]
    fn perceptron() {
        match types::perceptron(3f32, 9f32, 1920f32) {
            types::State::Inactive => assert!(false),
            _ => {}
        }

        match types::perceptron(4.3, 4., 1260.) {
            types::State::Inactive => assert!(true),
            types::State::Activate => assert!(false),
        }
    }
}
