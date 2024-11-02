use std::env;
use std::fs::File;
use std::io::BufReader;

use pyo3::prelude::*;

pub mod lex;
pub mod parse;
pub mod bytecode;
pub mod vm;
pub mod value;
pub mod utils;

#[pyfunction]
fn sum_as_string(a: usize, b: usize) -> PyResult<String> {
    Ok((a + b).to_string())
}

#[pyfunction]
fn raw_input(prompt: String) -> PyResult<()> {
    let file = File::open(&prompt).unwrap();

    let proto = parse::load(BufReader::new(file));
    vm::ExeState::new().execute(&proto, &Vec::new());
    Ok(())
}

#[pymodule]
#[pyo3(name = "LibCore")]
fn libcore(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(sum_as_string, m)?)?;
    m.add_function(wrap_pyfunction!(raw_input, m)?)?;
    Ok(())
}
