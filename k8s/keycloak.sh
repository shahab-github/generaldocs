docker network create keycloak-network

docker run -d --name postgresql \
  --network keycloak-network \
  -e POSTGRES_USER=keycloak_user \
  -e POSTGRES_PASSWORD=keycloak_password \
  -e POSTGRES_DB=keycloak_db \
  bitnami/postgresql:latest


docker run -p 8080:8080 \
  --name keycloak \
  --network keycloak-network \
  -e KEYCLOAK_ADMIN=admin \
  -e KEYCLOAK_ADMIN_PASSWORD=admin_password \
  -e KEYCLOAK_DATABASE_HOST=postgresql \
  -e KEYCLOAK_DATABASE_USER=keycloak_user \
  -e KEYCLOAK_DATABASE_PASSWORD=keycloak_password \
  -e KEYCLOAK_DATABASE_NAME=keycloak_db \
  bitnami/keycloak:latest
