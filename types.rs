pub enum State {
    Activate,
    Inactive,
}

pub fn perceptron(x1: f32, x2: f32, x3: f32) -> State {
    let w1 = 8.6f32;
    let w2 = 5f32;
    let w3 = 0.15f32;
    let bias = 280f32;

    match (x1*w1)+(x2*w2)+(x3*w3)-bias > 0f32 {
        true => {return State::Activate},
        false => {return State::Inactive}  
    }
}
