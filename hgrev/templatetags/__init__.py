def get_revision():
	from mercurial import ui, hg
	
	repo = hg.repository(ui.ui(), '.')
	
	fctx = repo.filectx(None, 'tip')
	
	return 'r%d:%s' % (fctx.rev(), fctx.hex()[:4])

REVISION = get_revision()
