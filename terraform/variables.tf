variable "rds_root_user" {
  description = "The username for the RDS instance"
  type        = string
  default = "root"
}

variable "rds_root_pass" {
  description = "The username for the RDS instance"
  type        = string
  default = "123456789"
}

variable "rds_db" {
  description = "The name of the RDS database"
  type        = string
default     = "shopdb"
}
