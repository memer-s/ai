mod types;
use types::{
    perceptron,
    State
};

fn main() {
    match perceptron(3f32, 9f32, 1920f32) {
        State::Inactive => println!("NO!"),
        State::Activate => println!("Yes!"),
    }

    match perceptron(4.3, 4., 1260.) {
        State::Inactive => println!("NO!"),
        State::Activate => println!("Yes!"),
    }
}
