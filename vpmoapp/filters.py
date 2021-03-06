from rest_framework import filters
from rest_framework import permissions
from guardian import shortcuts


class TeamListFilter(filters.BaseFilterBackend):
	""" A custom DRF FilterBackend that filters out only objects that a user has permissions for 
		FilterBackends are basically only effective for List Endpoints
	"""
	def filter_queryset(self, request, queryset, view):
		# Return objects for ANY permissions if request method is in ["GET", "HEAD", "OPTIONS"]
		if request.method in permissions.SAFE_METHODS:
			return shortcuts.get_objects_for_user(user=request.user,
				perms=["created_obj", "contribute_obj", "read_obj"], klass=queryset,
				accept_global_perms=False, any_perm=True)
		# Return objects for contribute and owner permissions if request method is POST
		elif request.method in ["POST"]:
			return shortcuts.get_objects_for_user(user=request.user,
				perms=["created_obj", "contribute_obj"], klass=queryset,
				accept_global_perms=False, any_perm=True)
		# Return objects for only owner permissions if request method is not in above conditionals
		else:
			return shortcuts.get_objects_for_user(user=request.user,
				perms=["created_obj"], klass=queryset, accept_global_perms=False,
				any_perm=True)