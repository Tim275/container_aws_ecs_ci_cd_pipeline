import drawio_diagrams as drawio

# Create a new diagram
diagram = drawio.Diagram("AWS_CICD_Pipeline")

# Add nodes and their corresponding AWS icons to the diagram
developer = diagram.add_icon("Person", "Developer", x=0, y=0)
code_commit = diagram.add_aws_icon("CodeCommit", "Code Commit", x=1, y=0)
s3_bucket = diagram.add_aws_icon("S3", "S3 Bucket", x=2, y=0)
code_build = diagram.add_aws_icon("CodeBuild", "Code Build", x=3, y=0)
ecr_repository = diagram.add_aws_icon("ECR", "ECR Repository", x=4, y=0)
code_deploy = diagram.add_aws_icon("CodeDeploy", "Code Deploy", x=5, y=0)
ecs_cluster = diagram.add_aws_icon("ECS", "ECS Cluster", x=6, y=0)
code_pipeline = diagram.add_aws_icon("CodePipeline", "Code Pipeline", x=3, y=1)
users = diagram.add_icon("Group", "Users", x=7, y=0)

# Add connections between the nodes
diagram.add_connection(developer, code_commit, label="1")
diagram.add_connection(code_commit, s3_bucket, label="2")
diagram.add_connection(s3_bucket, code_pipeline, label="3")
diagram.add_connection(code_build, s3_bucket, label="4")
diagram.add_connection(code_build, ecr_repository, label="5")
diagram.add_connection(code_pipeline, code_build, label="4")
diagram.add_connection(code_pipeline, code_deploy, label="6")
diagram.add_connection(code_deploy, ecs_cluster, label="7")
diagram.add_connection(ecs_cluster, users, label="8")

# Save the diagram to a file
file_path = "/mnt/data/AWS_CICD_Pipeline.drawio"
diagram.save(file_path)

file_path
