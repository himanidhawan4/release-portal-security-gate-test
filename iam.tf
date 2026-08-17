resource "aws_iam_policy" "sample_policy" {
  name        = "sample-pr-policy"
  description = "Sample IAM policy for security gate testing"

  policy = jsonencode({
    Version = "2012-10-17"

    Statement = [
      {
        Effect   = "Allow"
        Action   = "*"
        Resource = "*"
      }
    ]
  })
}
