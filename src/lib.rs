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

#[pymodule]
#[pyo3(name = "LibCore")]
fn libcore(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(sum_as_string, m)?)?;
    Ok(())
}
