resource "helm_release" "gameserver" {
  name       = "gameserver"
  chart      = "./chart"

  namespace  = "default"
}
