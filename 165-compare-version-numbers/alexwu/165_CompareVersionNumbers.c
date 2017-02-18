static int preprocess(char **p, char **pos, char *version) {
	int i = 0, leng = 0;

	if (*p) {
		if (NULL == (*pos = strchr(*p, '.'))) {
			*pos = &version[strlen(version) - 1];
			leng = *pos - *p + 1;
			*pos = *p;
			*p = NULL;
		} else {
			leng = *pos - *p;
			*pos = *p;
			*p = *pos + leng + 1;
		}

		for (i = 0; i < leng; ++i, (*pos)++) {
			if ('0' != **pos) break;
		}

		return leng - i;
	}

	return 0;
}

int compareVersion(char* version1, char* version2) {
	char *p1 = version1;
	char *p2 = version2;
	char *pos1 = p1;
	char *pos2 = p2;
	int i = 0, leng1 = 0, leng2 = 0;

	while (NULL != p1 || NULL != p2) {
		leng1 = preprocess(&p1, &pos1, version1);
		leng2 = preprocess(&p2, &pos2, version2);

		if (leng1 > leng2) return 1;
		if (leng1 < leng2) return -1;

		for (i = 0; i < leng1; ++i, pos1++, pos2++) {
			if (*pos1 > *pos2) return 1;
			if (*pos1 < *pos2) return -1;
		}
	}

	return 0;
}
