def get_revision():
	try:
		from hgrev import settings, ui, hg
		
		repo = hg.repository(ui.ui(), settings.HGREV_HG_PATH)
		fctx = repo.filectx(None, 'tip')
		
		return 'r%d:%s' % (fctx.rev(), fctx.hex()[:4])
	except Exception:
		return ''

REVISION = get_revision()
