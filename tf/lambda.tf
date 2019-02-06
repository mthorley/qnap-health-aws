

/*
FIXME: Create this role rather than source it
*/
data "aws_iam_role" "lambda_exec_role" {
  name = "CMLambdaExecutionRole"
}

resource "aws_lambda_function" "qnap_temp_lambda" {
  filename         = "../qnapTempLambda.zip"
  function_name    = "qnap_temp"
  role             = "${aws_iam_role.lambda_exec_role.arn}"
  handler          = "lambda_handler"
  source_code_hash = "${base64sha256(file("../qnapTempLambda.zip"))}"
  runtime          = "python3.7"

  environment {
    variables = {
      foo = "bar"
    }
  }
}


