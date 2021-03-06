data "terraform_remote_state" "vpc" {
  backend = "s3"

  config = {
    bucket = var.terraform_platform_state_s3_bucket
    key    = var.vpc_terraform_state_key
    region = var.aws_region
  }
}

data "terraform_remote_state" "security-groups-k8s" {
  backend = "s3"

  config = {
    bucket = var.terraform_platform_state_s3_bucket
    key    = var.security-groups-k8s_terraform_state_key
    region = var.aws_region
  }
}
